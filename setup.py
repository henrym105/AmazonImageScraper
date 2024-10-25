import os
import sys
from pathlib import Path

def create_directories():
    """Create necessary project directories"""
    try:
        Path('data').mkdir(exist_ok=True)
        Path('logs').mkdir(exist_ok=True)
        print("Project directories created successfully")
        return True
    except Exception as e:
        print(f"Failed to create directories: {str(e)}")
        return False

def main():
    print("Setting up Amazon Product Image Scraper...")
    
    success = True
    
    # Create necessary directories
    if not create_directories():
        success = False
        print("Failed to create necessary directories")
        sys.exit(1)
    
    print("Installing Python 3.11...")
    try:
        programming_language_install_tool(programming_languages=["python-3.11"])
    except Exception as e:
        print(f"Failed to install Python: {str(e)}")
        success = False
    
    print("Installing required packages...")
    try:
        packager_install_tool(
            programming_language="python",
            dependency_list=["requests", "beautifulsoup4"]
        )
    except Exception as e:
        print(f"Failed to install packages: {str(e)}")
        success = False
    
    if success:
        print("\nSetup completed successfully!")
        print("\nYou can now run the scraper using:")
        print("python main.py")
    else:
        print("\nSetup failed. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
