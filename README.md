# Inventory Management System

A Flask-based web application for managing inventory across multiple locations. This system allows you to track products, manage locations, record movements, and generate balance reports.

## Features

- **Product Management**: Add, edit, and delete products with unique IDs and descriptions
- **Location Management**: Manage multiple warehouses and storage locations
- **Movement Tracking**: Record incoming and outgoing product movements between locations
- **Balance Reports**: View current inventory balance for each product in each location
- **Modern UI**: Clean, responsive interface built with Bootstrap 5

## Database Schema

### Tables

1. **Product** (`product_id`, `name`, `description`)
2. **Location** (`location_id`, `name`, `address`)
3. **ProductMovement** (`movement_id`, `timestamp`, `from_location`, `to_location`, `product_id`, `qty`)

### Key Features

- Primary keys are text/varchar for easy identification
- Movements can have either `from_location` or `to_location` (or both)
- Automatic timestamp tracking for all movements
- Balance calculation based on incoming vs outgoing quantities

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd inventory
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database with sample data**
   ```bash
   python add_sample_data.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your web browser and navigate to `http://localhost:5000`

## Usage

### Dashboard
The dashboard provides an overview of your inventory system with:
- Count of products, locations, and movements
- Quick access buttons to add new items
- System information and help

### Managing Products
1. Navigate to "Products" from the main menu
2. Click "Add New Product" to create a new product
3. Fill in the Product ID, Name, and Description
4. Use Edit/Delete buttons to modify existing products

### Managing Locations
1. Navigate to "Locations" from the main menu
2. Click "Add New Location" to create a new location
3. Fill in the Location ID, Name, and Address
4. Use Edit/Delete buttons to modify existing locations

### Recording Movements
1. Navigate to "Movements" from the main menu
2. Click "Add New Movement" to record a movement
3. Select the product and at least one location (from or to)
4. Enter the quantity being moved
5. Use Edit/Delete buttons to modify existing movements

### Viewing Balance Reports
1. Navigate to "Balance Report" from the main menu
2. View current inventory balance for all products in all locations
3. Only locations with positive stock are displayed
4. Use the Print button to generate a printable report

## Sample Data

The application comes with pre-loaded sample data including:
- 4 sample products (Laptop, Mouse, Keyboard, Monitor)
- 4 sample locations (Main Warehouse, Store Front, Storage Room A, Online Orders)
- 20 sample movements demonstrating various scenarios

## Technical Details

### Technology Stack
- **Backend**: Flask (Python web framework)
- **Database**: SQLite (included with Python)
- **Frontend**: HTML5, Bootstrap 5, Bootstrap Icons
- **ORM**: Flask-SQLAlchemy
- **Forms**: Flask-WTF with WTForms

### Key Features
- Responsive design that works on desktop and mobile
- Form validation with user-friendly error messages
- Flash messages for user feedback
- Print-friendly balance reports
- Clean, modern UI with Bootstrap components

### File Structure
```
inventory/
├── app.py                 # Main Flask application
├── add_sample_data.py     # Script to populate sample data
├── requirements.txt       # Python dependencies
├── inventory.db          # SQLite database (created on first run)
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Dashboard
│   ├── products.html     # Product listing
│   ├── product_form.html # Product add/edit form
│   ├── locations.html    # Location listing
│   ├── location_form.html # Location add/edit form
│   ├── movements.html    # Movement listing
│   ├── movement_form.html # Movement add/edit form
│   └── balance.html      # Balance report
└── README.md             # This file
```

## API Endpoints

- `GET /` - Dashboard
- `GET /products` - List all products
- `GET /products/add` - Add new product form
- `POST /products/add` - Create new product
- `GET /products/edit/<id>` - Edit product form
- `POST /products/edit/<id>` - Update product
- `GET /products/delete/<id>` - Delete product
- `GET /locations` - List all locations
- `GET /locations/add` - Add new location form
- `POST /locations/add` - Create new location
- `GET /locations/edit/<id>` - Edit location form
- `POST /locations/edit/<id>` - Update location
- `GET /locations/delete/<id>` - Delete location
- `GET /movements` - List all movements
- `GET /movements/add` - Add new movement form
- `POST /movements/add` - Create new movement
- `GET /movements/edit/<id>` - Edit movement form
- `POST /movements/edit/<id>` - Update movement
- `GET /movements/delete/<id>` - Delete movement
- `GET /balance` - Balance report

## Development

### Running in Development Mode
```bash
python app.py
```
The application will run in debug mode with auto-reload enabled.

### Database Reset
To reset the database with fresh sample data:
```bash
python add_sample_data.py
```

## Screenshots

### Dashboard
<img width="1919" height="970" alt="image" src="https://github.com/user-attachments/assets/3c07adef-7245-4761-b65c-0cfcb1ec053d" />


### Products Management
<img width="1919" height="971" alt="image" src="https://github.com/user-attachments/assets/257c5997-0975-4a34-9f62-e37bd52af784" />


### Locations Management
<img width="1916" height="969" alt="image" src="https://github.com/user-attachments/assets/c2c916a5-0aff-4632-aaaf-8fcd9a587e73" />


### Movement Tracking
<img width="1918" height="970" alt="image" src="https://github.com/user-attachments/assets/6e8a0af1-64a5-4db8-b04c-c08e289a004d" />


### Balance Report
<img width="1919" height="967" alt="image" src="https://github.com/user-attachments/assets/3ec63b37-c2c7-4e66-a048-2d4d7e4b37c5" />



## License

This project is created as part of a Flask hiring test and is for demonstration purposes.


