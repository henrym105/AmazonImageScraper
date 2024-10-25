import os
import logging
import sys
from scraper.constants import CATEGORIES, LOG_FILE, DATA_DIR
from scraper.utils import setup_logging, create_directories
from scraper.amazon_scraper import AmazonScraper

def main():
    try:
        # Set up logging
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        setup_logging(LOG_FILE)
        
        logging.info("Starting Amazon product image scraper")
        logging.info(f"Python version: {sys.version}")
        
        # Create necessary directories
        create_directories(DATA_DIR, CATEGORIES.keys())
        logging.info(f"Created directories for categories in {DATA_DIR}")
        
        # Initialize scraper
        scraper = AmazonScraper(DATA_DIR)
        
        # Track success and failure counts
        success_count = 0
        failure_count = 0
        
        # Scrape each category
        for category_name, category_url in CATEGORIES.items():
            try:
                logging.info(f"Starting to scrape category: {category_name}")
                scraper.scrape_category(category_name, category_url)
                success_count += 1
                logging.info(f"Successfully completed scraping for category: {category_name}")
            except Exception as e:
                failure_count += 1
                logging.error(f"Failed to scrape category {category_name}: {str(e)}", exc_info=True)
                continue
        
        # Log final statistics
        logging.info(f"Scraping completed. Success: {success_count}, Failures: {failure_count}")
        
    except Exception as e:
        logging.critical(f"Critical error in main process: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
