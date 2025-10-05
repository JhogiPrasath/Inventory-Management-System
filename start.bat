@echo off
echo Inventory Management System - Windows Startup
echo ============================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting the application...
python start.py
pause
