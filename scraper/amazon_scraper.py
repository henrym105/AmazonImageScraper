import os
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import json
from .constants import AMAZON_BASE_URL, MAX_IMAGES_PER_CATEGORY
from .utils import get_random_user_agent, random_delay, download_image, is_valid_image_url

class AmazonScraper:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.session = requests.Session()
        self.headers = {
            'User-Agent': get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        self.session.headers.update(self.headers)

    def get_page(self, url):
        """Fetch page content with error handling and retries"""
        tries = 3
        
        for attempt in range(tries):
            try:
                logging.info(f"Attempting to fetch {url} (attempt {attempt + 1}/{tries})")
                response = self.session.get(url, timeout=15)
                response.raise_for_status()
                logging.info(f"Successfully fetched page: {url}")
                return response.text
            except requests.RequestException as e:
                logging.error(f"Attempt {attempt + 1}/{tries} failed for {url}: {str(e)}")
                if attempt == tries - 1:
                    raise
                random_delay()
        
        return None

    def extract_image_urls(self, html_content):
        """Extract product image URLs from HTML content"""
        soup = BeautifulSoup(html_content, 'html.parser')
        image_urls = set()
        
        logging.info("Searching for image elements in the page")
        
        # Multiple ways to find product images
        selectors = [
            'img.s-image',  # Main product images
            'img[data-old-hires]',  # High-res product images
            'img[data-a-dynamic-image]',  # Dynamic images
            'img[srcset]'  # Responsive images
        ]
        
        for selector in selectors:
            images = soup.select(selector)
            logging.info(f"Found {len(images)} images using selector: {selector}")
            
            for img in images:
                # Try different attributes where image URLs might be stored
                url = None
                
                # Check data-a-dynamic-image first (contains multiple sizes in JSON)
                dynamic_image = img.get('data-a-dynamic-image')
                if isinstance(dynamic_image, str):
                    try:
                        urls_dict = json.loads(dynamic_image)
                        if urls_dict and isinstance(urls_dict, dict):
                            # Get the URL with the highest resolution
                            url = max(urls_dict.items(), key=lambda x: x[1][0] * x[1][1])[0]
                    except (json.JSONDecodeError, ValueError, IndexError):
                        pass
                
                # Fallback to other attributes
                if not url:
                    srcset = img.get('srcset', '')
                    if isinstance(srcset, str) and srcset:
                        try:
                            url = srcset.split(',')[0].split()[0]
                        except (IndexError, AttributeError):
                            pass
                    
                    if not url:
                        url = img.get('data-old-hires') or img.get('src')
                
                if isinstance(url, str) and url and is_valid_image_url(url):
                    if not url.startswith('http'):
                        url = urljoin(AMAZON_BASE_URL, url)
                    image_urls.add(url)
                    logging.debug(f"Found valid image URL: {url}")
        
        return list(image_urls)

    def scrape_category(self, category_name, category_url):
        """Scrape images for a specific category"""
        logging.info(f"Starting to scrape category: {category_name}")
        
        category_dir = os.path.join(self.data_dir, category_name)
        full_url = urljoin(AMAZON_BASE_URL, category_url)
        
        try:
            html_content = self.get_page(full_url)
            if not html_content:
                logging.error(f"Failed to get content for category: {category_name}")
                return
            
            image_urls = self.extract_image_urls(html_content)
            logging.info(f"Found {len(image_urls)} images in {category_name}")
            
            for idx, image_url in enumerate(image_urls[:MAX_IMAGES_PER_CATEGORY]):
                if idx >= MAX_IMAGES_PER_CATEGORY:
                    break
                    
                filename = f"{category_name}_{idx + 1}.jpg"
                filepath = os.path.join(category_dir, filename)
                
                if download_image(image_url, filepath):
                    logging.info(f"Successfully downloaded: {filename}")
                else:
                    logging.warning(f"Failed to download: {filename}")
                
                random_delay()
                
        except Exception as e:
            logging.error(f"Error scraping category {category_name}: {str(e)}")
