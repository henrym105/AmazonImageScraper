import os
import random
import time
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from .constants import USER_AGENTS, MIN_DELAY, MAX_DELAY

def setup_logging(log_file):
    """Set up logging configuration"""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def create_directories(base_dir, categories):
    """Create directory structure for storing images"""
    for category in categories:
        os.makedirs(os.path.join(base_dir, category), exist_ok=True)

def get_random_user_agent():
    """Return a random user agent from the list"""
    return random.choice(USER_AGENTS)

def random_delay():
    """Implement a random delay between requests"""
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    time.sleep(delay)

def download_image(url, filepath):
    """Download an image from URL and save it to filepath"""
    headers = {
        'User-Agent': get_random_user_agent(),
        'Accept': 'image/webp,*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.amazon.com/',
    }
    
    try:
        logging.info(f"Attempting to download image from: {url}")
        response = requests.get(url, headers=headers, stream=True, timeout=15)
        response.raise_for_status()
        
        # Verify content type is an image
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            logging.error(f"Invalid content type for {url}: {content_type}")
            return False
        
        # Get file size
        file_size = int(response.headers.get('content-length', 0))
        if file_size < 1000:  # Skip if file is too small (likely an error image)
            logging.warning(f"Skipping {url} - file too small ({file_size} bytes)")
            return False
            
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        logging.info(f"Successfully downloaded image to: {filepath}")
        return True
        
    except Exception as e:
        logging.error(f"Error downloading image from {url}: {str(e)}")
        return False

def is_valid_image_url(url):
    """Check if URL is a valid image URL"""
    if not url:
        return False
    
    # Clean up the URL
    url = url.strip().lower()
    
    # Check if it's a valid image extension
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    has_valid_extension = any(url.endswith(ext) for ext in valid_extensions)
    
    # Check for common Amazon image patterns
    is_amazon_image = ('images-amazon' in url or 'images/I' in url)
    
    return has_valid_extension or is_amazon_image
