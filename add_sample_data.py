from app import app, db, Product, Location, ProductMovement
from datetime import datetime, timedelta
import random

def add_sample_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Add sample products
        products_data = [
            {'product_id': 'P001', 'name': 'Laptop Computer', 'description': 'High-performance laptop for business use'},
            {'product_id': 'P002', 'name': 'Wireless Mouse', 'description': 'Ergonomic wireless mouse with USB receiver'},
            {'product_id': 'P003', 'name': 'Mechanical Keyboard', 'description': 'RGB mechanical keyboard with blue switches'},
            {'product_id': 'P004', 'name': 'Monitor 24"', 'description': '24-inch LED monitor with Full HD resolution'},
        ]
        
        for product_data in products_data:
            product = Product(**product_data)
            db.session.add(product)
        
        # Add sample locations
        locations_data = [
            {'location_id': 'L001', 'name': 'Main Warehouse', 'address': '123 Industrial Blvd, City, State 12345'},
            {'location_id': 'L002', 'name': 'Store Front', 'address': '456 Main Street, City, State 12345'},
            {'location_id': 'L003', 'name': 'Storage Room A', 'address': '789 Storage Lane, City, State 12345'},
            {'location_id': 'L004', 'name': 'Online Orders', 'address': 'Virtual location for online sales'},
        ]
        
        for location_data in locations_data:
            location = Location(**location_data)
            db.session.add(location)
        
        db.session.commit()
        
        # Add sample movements
        movements_data = [
            # Initial stock - incoming to warehouse
            {'movement_id': 'M001', 'product_id': 'P001', 'to_location': 'L001', 'qty': 50},
            {'movement_id': 'M002', 'product_id': 'P002', 'to_location': 'L001', 'qty': 100},
            {'movement_id': 'M003', 'product_id': 'P003', 'to_location': 'L001', 'qty': 75},
            {'movement_id': 'M004', 'product_id': 'P004', 'to_location': 'L001', 'qty': 30},
            
            # Move some products to store front
            {'movement_id': 'M005', 'product_id': 'P001', 'from_location': 'L001', 'to_location': 'L002', 'qty': 10},
            {'movement_id': 'M006', 'product_id': 'P002', 'from_location': 'L001', 'to_location': 'L002', 'qty': 25},
            {'movement_id': 'M007', 'product_id': 'P003', 'from_location': 'L001', 'to_location': 'L002', 'qty': 15},
            {'movement_id': 'M008', 'product_id': 'P004', 'from_location': 'L001', 'to_location': 'L002', 'qty': 8},
            
            # Move some products to storage room
            {'movement_id': 'M009', 'product_id': 'P001', 'from_location': 'L001', 'to_location': 'L003', 'qty': 5},
            {'movement_id': 'M010', 'product_id': 'P002', 'from_location': 'L001', 'to_location': 'L003', 'qty': 20},
            
            # Online sales (outgoing from store)
            {'movement_id': 'M011', 'product_id': 'P001', 'from_location': 'L002', 'to_location': 'L004', 'qty': 3},
            {'movement_id': 'M012', 'product_id': 'P002', 'from_location': 'L002', 'to_location': 'L004', 'qty': 8},
            {'movement_id': 'M013', 'product_id': 'P003', 'from_location': 'L002', 'to_location': 'L004', 'qty': 5},
            {'movement_id': 'M014', 'product_id': 'P004', 'from_location': 'L002', 'to_location': 'L004', 'qty': 2},
            
            # More incoming stock
            {'movement_id': 'M015', 'product_id': 'P001', 'to_location': 'L001', 'qty': 20},
            {'movement_id': 'M016', 'product_id': 'P002', 'to_location': 'L001', 'qty': 50},
            
            # Transfer between locations
            {'movement_id': 'M017', 'product_id': 'P001', 'from_location': 'L003', 'to_location': 'L002', 'qty': 2},
            {'movement_id': 'M018', 'product_id': 'P002', 'from_location': 'L003', 'to_location': 'L002', 'qty': 10},
            
            # More online sales
            {'movement_id': 'M019', 'product_id': 'P001', 'from_location': 'L002', 'to_location': 'L004', 'qty': 4},
            {'movement_id': 'M020', 'product_id': 'P003', 'from_location': 'L002', 'to_location': 'L004', 'qty': 3},
        ]
        
        # Add movements with timestamps
        base_time = datetime.utcnow() - timedelta(days=30)
        for i, movement_data in enumerate(movements_data):
            movement = ProductMovement(
                movement_id=movement_data['movement_id'],
                product_id=movement_data['product_id'],
                from_location=movement_data.get('from_location'),
                to_location=movement_data.get('to_location'),
                qty=movement_data['qty'],
                timestamp=base_time + timedelta(hours=i*2)
            )
            db.session.add(movement)
        
        db.session.commit()
        print("Sample data added successfully!")
        print(f"Added {len(products_data)} products")
        print(f"Added {len(locations_data)} locations")
        print(f"Added {len(movements_data)} movements")

if __name__ == '__main__':
    add_sample_data()
