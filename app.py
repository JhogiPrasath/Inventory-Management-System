from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Product(db.Model):
    product_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Product {self.product_id}: {self.name}>'

class Location(db.Model):
    location_id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Location {self.location_id}: {self.name}>'

class ProductMovement(db.Model):
    movement_id = db.Column(db.String(50), primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    from_location = db.Column(db.String(50), db.ForeignKey('location.location_id'), nullable=True)
    to_location = db.Column(db.String(50), db.ForeignKey('location.location_id'), nullable=True)
    product_id = db.Column(db.String(50), db.ForeignKey('product.product_id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    
    # Relationships
    product = db.relationship('Product', backref='movements')
    from_loc = db.relationship('Location', foreign_keys=[from_location], backref='outgoing_movements')
    to_loc = db.relationship('Location', foreign_keys=[to_location], backref='incoming_movements')
    
    def __repr__(self):
        return f'<Movement {self.movement_id}: {self.qty} {self.product_id} from {self.from_location} to {self.to_location}>'

# Forms
class ProductForm(FlaskForm):
    product_id = StringField('Product ID', validators=[DataRequired()])
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Save Product')

class LocationForm(FlaskForm):
    location_id = StringField('Location ID', validators=[DataRequired()])
    name = StringField('Location Name', validators=[DataRequired()])
    address = TextAreaField('Address')
    submit = SubmitField('Save Location')

class MovementForm(FlaskForm):
    movement_id = StringField('Movement ID', validators=[DataRequired()])
    product_id = SelectField('Product', coerce=str, validators=[DataRequired()])
    from_location = SelectField('From Location', coerce=str)
    to_location = SelectField('To Location', coerce=str)
    qty = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Save Movement')
    
    def __init__(self, *args, **kwargs):
        super(MovementForm, self).__init__(*args, **kwargs)
        try:
            self.product_id.choices = [(p.product_id, f"{p.product_id} - {p.name}") for p in Product.query.all()]
            self.from_location.choices = [('', 'Select Location')] + [(l.location_id, f"{l.location_id} - {l.name}") for l in Location.query.all()]
            self.to_location.choices = [('', 'Select Location')] + [(l.location_id, f"{l.location_id} - {l.name}") for l in Location.query.all()]
        except Exception:
            # If database is not initialized, provide empty choices
            self.product_id.choices = []
            self.from_location.choices = [('', 'Select Location')]
            self.to_location.choices = [('', 'Select Location')]

# Routes
@app.route('/')
def index():
    products_count = Product.query.count()
    locations_count = Location.query.count()
    movements_count = ProductMovement.query.count()
    return render_template('index.html', 
                         products_count=products_count,
                         locations_count=locations_count,
                         movements_count=movements_count)

@app.route('/products')
def products():
    search_query = request.args.get('search', '').strip()
    if search_query:
        products = Product.query.filter(
            (Product.product_id.contains(search_query)) |
            (Product.name.contains(search_query)) |
            (Product.description.contains(search_query))
        ).all()
    else:
        products = Product.query.all()
    return render_template('products.html', products=products, search_query=search_query)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            product_id=form.product_id.data,
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('products'))
    return render_template('product_form.html', form=form, title='Add Product')

@app.route('/products/edit/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('products'))
    return render_template('product_form.html', form=form, title='Edit Product')

@app.route('/products/delete/<product_id>')
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    # Check if there are any movements referencing this product
    movements = ProductMovement.query.filter_by(product_id=product_id).all()
    if movements:
        flash(f'Cannot delete product "{product.name}" because it has {len(movements)} movement(s) associated with it. Please delete the movements first.', 'error')
        return redirect(url_for('products'))
    
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('products'))

@app.route('/locations')
def locations():
    search_query = request.args.get('search', '').strip()
    if search_query:
        locations = Location.query.filter(
            (Location.location_id.contains(search_query)) |
            (Location.name.contains(search_query)) |
            (Location.address.contains(search_query))
        ).all()
    else:
        locations = Location.query.all()
    return render_template('locations.html', locations=locations, search_query=search_query)

@app.route('/locations/add', methods=['GET', 'POST'])
def add_location():
    form = LocationForm()
    if form.validate_on_submit():
        location = Location(
            location_id=form.location_id.data,
            name=form.name.data,
            address=form.address.data
        )
        db.session.add(location)
        db.session.commit()
        flash('Location added successfully!', 'success')
        return redirect(url_for('locations'))
    return render_template('location_form.html', form=form, title='Add Location')

@app.route('/locations/edit/<location_id>', methods=['GET', 'POST'])
def edit_location(location_id):
    location = Location.query.get_or_404(location_id)
    form = LocationForm(obj=location)
    if form.validate_on_submit():
        location.name = form.name.data
        location.address = form.address.data
        db.session.commit()
        flash('Location updated successfully!', 'success')
        return redirect(url_for('locations'))
    return render_template('location_form.html', form=form, title='Edit Location')

@app.route('/locations/delete/<location_id>')
def delete_location(location_id):
    location = Location.query.get_or_404(location_id)
    
    # Check if there are any movements referencing this location
    from_movements = ProductMovement.query.filter_by(from_location=location_id).all()
    to_movements = ProductMovement.query.filter_by(to_location=location_id).all()
    total_movements = len(from_movements) + len(to_movements)
    
    if total_movements > 0:
        flash(f'Cannot delete location "{location.name}" because it has {total_movements} movement(s) associated with it. Please delete the movements first.', 'error')
        return redirect(url_for('locations'))
    
    db.session.delete(location)
    db.session.commit()
    flash('Location deleted successfully!', 'success')
    return redirect(url_for('locations'))

@app.route('/movements')
def movements():
    search_query = request.args.get('search', '').strip()
    if search_query:
        movements = ProductMovement.query.join(Product).join(Location, 
            (ProductMovement.from_location == Location.location_id) | 
            (ProductMovement.to_location == Location.location_id)
        ).filter(
            (ProductMovement.movement_id.contains(search_query)) |
            (Product.product_id.contains(search_query)) |
            (Product.name.contains(search_query)) |
            (Location.location_id.contains(search_query)) |
            (Location.name.contains(search_query))
        ).order_by(ProductMovement.timestamp.desc()).all()
    else:
        movements = ProductMovement.query.order_by(ProductMovement.timestamp.desc()).all()
    return render_template('movements.html', movements=movements, search_query=search_query)

@app.route('/movements/add', methods=['GET', 'POST'])
def add_movement():
    # Check if there are products and locations
    if Product.query.count() == 0:
        flash('Please add some products before creating movements.', 'error')
        return redirect(url_for('add_product'))
    if Location.query.count() == 0:
        flash('Please add some locations before creating movements.', 'error')
        return redirect(url_for('add_location'))
    
    form = MovementForm()
    if form.validate_on_submit():
        # Validate that at least one location is selected
        if not form.from_location.data and not form.to_location.data:
            flash('Please select at least one location (from or to)', 'error')
            return render_template('movement_form.html', form=form, title='Add Movement')
        
        movement = ProductMovement(
            movement_id=form.movement_id.data,
            product_id=form.product_id.data,
            from_location=form.from_location.data if form.from_location.data else None,
            to_location=form.to_location.data if form.to_location.data else None,
            qty=form.qty.data
        )
        db.session.add(movement)
        db.session.commit()
        flash('Movement added successfully!', 'success')
        return redirect(url_for('movements'))
    return render_template('movement_form.html', form=form, title='Add Movement')

@app.route('/movements/edit/<movement_id>', methods=['GET', 'POST'])
def edit_movement(movement_id):
    movement = ProductMovement.query.get_or_404(movement_id)
    form = MovementForm(obj=movement)
    if form.validate_on_submit():
        if not form.from_location.data and not form.to_location.data:
            flash('Please select at least one location (from or to)', 'error')
            return render_template('movement_form.html', form=form, title='Edit Movement')
        
        movement.product_id = form.product_id.data
        movement.from_location = form.from_location.data if form.from_location.data else None
        movement.to_location = form.to_location.data if form.to_location.data else None
        movement.qty = form.qty.data
        db.session.commit()
        flash('Movement updated successfully!', 'success')
        return redirect(url_for('movements'))
    return render_template('movement_form.html', form=form, title='Edit Movement')

@app.route('/movements/delete/<movement_id>')
def delete_movement(movement_id):
    movement = ProductMovement.query.get_or_404(movement_id)
    db.session.delete(movement)
    db.session.commit()
    flash('Movement deleted successfully!', 'success')
    return redirect(url_for('movements'))

@app.route('/movements/delete-all')
def delete_all_movements():
    movements = ProductMovement.query.all()
    count = len(movements)
    
    for movement in movements:
        db.session.delete(movement)
    
    db.session.commit()
    flash(f'Successfully deleted {count} movements. You can now delete products and locations.', 'success')
    return redirect(url_for('movements'))

@app.route('/balance')
def balance():
    # Get all products and locations
    products = Product.query.all()
    locations = Location.query.all()
    
    # Calculate balance for each product in each location
    balance_data = []
    for product in products:
        for location in locations:
            # Calculate incoming quantity (to_location = this location)
            incoming = db.session.query(db.func.sum(ProductMovement.qty)).filter(
                ProductMovement.to_location == location.location_id,
                ProductMovement.product_id == product.product_id
            ).scalar() or 0
            
            # Calculate outgoing quantity (from_location = this location)
            outgoing = db.session.query(db.func.sum(ProductMovement.qty)).filter(
                ProductMovement.from_location == location.location_id,
                ProductMovement.product_id == product.product_id
            ).scalar() or 0
            
            balance = incoming - outgoing
            if balance > 0:  # Only show locations with positive balance
                balance_data.append({
                    'product_id': product.product_id,
                    'product_name': product.name,
                    'location_id': location.location_id,
                    'location_name': location.name,
                    'balance': balance
                })
    
    return render_template('balance.html', balance_data=balance_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
