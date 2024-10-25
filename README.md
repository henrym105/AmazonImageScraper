# Amazon Product Image Scraper

A Python script that scrapes product images from Amazon for specific product categories. The scraper is designed with built-in rate limiting and error handling to ensure reliable data collection.

## Description

This project provides a robust solution for collecting product images from Amazon across 10 specific categories. It includes features like:
- Rate limiting to respect Amazon's servers
- User agent rotation to prevent blocking
- Comprehensive error handling and logging
- Support for multiple product categories
- Automatic image validation and filtering

## Installation

1. Clone the repository:
```bash
git clone https://github.com/henrym105/AmazonImageScraper.git
cd amazon-product-image-scraper
```

2. Install the required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage

Run the scraper using:
```bash
python main.py
```

The script will:
1. Create necessary directories for each category
2. Download images for each category (max 50 images per category)
3. Save logs in the `logs` directory
4. Store images in category-specific folders under the `data` directory

## Supported Categories

The scraper currently supports the following product categories:
1. Backpack
2. Bike (Bicycle)
3. Calculator
4. Headphones
5. Keyboard (Computer Keyboard)
6. Laptop
7. Monitor (Computer Monitor)
8. Mouse (Computer Mouse)
9. Mug (Coffee Mug)
10. Projector

## Rate Limiting and Best Practices

To ensure responsible scraping and avoid being blocked:
- Random delays between requests (2-5 seconds)
- User agent rotation
- Maximum of 50 images per category
- Automatic retry mechanism for failed requests
- Comprehensive error logging

## Directory Structure

```
├── data/           # Downloaded images (gitignored)
├── logs/           # Log files (gitignored)
├── scraper/        # Main scraper module
│   ├── constants.py
│   ├── utils.py
│   └── amazon_scraper.py
└── main.py         # Entry point
```

## Notes

- This scraper is for educational purposes only
- Be mindful of Amazon's terms of service and robots.txt
- Consider implementing additional delay if running for extended periods
- Check the logs directory for detailed execution information
