#!/usr/bin/env python3
"""
Startup script for the Inventory Management System
This script will initialize the database with sample data and start the Flask application
"""

import os
import sys
import subprocess

def main():
    print("Inventory Management System - Startup Script")
    print("=" * 50)
    
    # Check if requirements are installed
    print("Checking dependencies...")
    try:
        import flask
        import flask_sqlalchemy
        import flask_wtf
        import wtforms
        print("[OK] All dependencies are installed")
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    # Initialize database with sample data
    print("\nInitializing database with sample data...")
    try:
        from add_sample_data import add_sample_data
        add_sample_data()
        print("[OK] Database initialized successfully")
    except Exception as e:
        print(f"[ERROR] Failed to initialize database: {e}")
        return False
    
    # Start the Flask application
    print("\nStarting Flask application...")
    print("The application will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\nServer stopped by user")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to start server: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
