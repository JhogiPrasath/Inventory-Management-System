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
![Dashboard](screenshots/dashboard.png)
*The main dashboard shows system overview with animated stats cards, quick access buttons, and helpful tips section.*

### Products Management
![Products Page](screenshots/products.png)
*Clean interface for managing products with search functionality, add, edit, and delete capabilities.*

### Product Search
![Product Search](screenshots/product-search.png)
*Real-time search functionality across product ID, name, and description fields.*

### Locations Management
![Locations Page](screenshots/locations.png)
*Easy-to-use location management with address tracking and search capabilities.*

### Movement Tracking
![Movements Page](screenshots/movements.png)
*Comprehensive movement tracking with support for incoming, outgoing, and transfer movements.*

### Movement Search
![Movement Search](screenshots/movement-search.png)
*Advanced search functionality across movements, products, and locations.*

### Balance Report
![Balance Report](screenshots/balance.png)
*Detailed balance report showing current inventory levels across all locations with print functionality.*

### Add Product Form
![Add Product](screenshots/add-product.png)
*Modern form design with validation and helpful tooltips.*

### Add Movement Form
![Add Movement](screenshots/add-movement.png)
*Intuitive movement form with dropdown selections and validation.*

### Mobile Responsive Design
![Mobile View](screenshots/mobile.png)
*Fully responsive design that works seamlessly on mobile devices.*

## How to Take Screenshots

To add screenshots to your README:

1. **Create a screenshots folder (if it doesn't exist):**
   ```bash
   mkdir screenshots
   ```

2. **Take screenshots of each page:**
   - Dashboard: `http://localhost:5000`
   - Products: `http://localhost:5000/products`
   - Product Search: `http://localhost:5000/products?search=laptop`
   - Locations: `http://localhost:5000/locations`
   - Movements: `http://localhost:5000/movements`
   - Movement Search: `http://localhost:5000/movements?search=P001`
   - Balance Report: `http://localhost:5000/balance`
   - Add Product: `http://localhost:5000/products/add`
   - Add Movement: `http://localhost:5000/movements/add`

3. **Save screenshots with these exact names:**
   - `dashboard.png`
   - `products.png`
   - `product-search.png`
   - `locations.png`
   - `movements.png`
   - `movement-search.png`
   - `balance.png`
   - `add-product.png`
   - `add-movement.png`
   - `mobile.png` (optional - mobile view)

4. **Recommended screenshot settings:**
   - Use a modern browser (Chrome, Firefox, Edge)
   - Set browser zoom to 100%
   - Use a resolution of 1920x1080 or higher
   - Capture the full page or main content area
   - Ensure the application is running with sample data

5. **Taking screenshots:**
   - Use the URLs listed above to open pages individually
   - Take screenshots of each page as you navigate through them

## License

This project is created as part of a Flask hiring test and is for demonstration purposes.

## Contact

For questions or support, please contact the development team.
