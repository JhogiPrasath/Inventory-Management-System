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

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

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



