#!/bin/bash

# Exit on error
set -e

echo "Setting up Amazon Product Image Scraper..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1clear
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p data logs

# Create virtual environment
python -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
if ! pip install -r requirements.txt; then
    echo "--------> Error: Failed to install required packages <--------"
    exit 1
fi

echo " "
echo "Setup completed successfully!"
echo " "
