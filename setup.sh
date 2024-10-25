#!/bin/bash

# Exit on error
set -e

echo "Setting up Amazon Product Image Scraper..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Create necessary directories
echo "Creating directories..."
mkdir -p data logs

# Install required packages
echo "Installing required packages..."
if ! pip install -r requirements.txt; then
    echo "Error: Failed to install required packages"
    exit 1
fi

echo "Setup completed successfully!"
echo "You can now run the scraper using: python3 main.py"
