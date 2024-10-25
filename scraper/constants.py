# Base URL and category paths
AMAZON_BASE_URL = "https://www.amazon.com"
CATEGORIES = {
    "backpack": "/s?k=backpack",
    "bike": "/s?k=bicycle",
    "calculator": "/s?k=calculator",
    "headphones": "/s?k=headphones",
    "keyboard": "/s?k=computer+keyboard",
    "laptop": "/s?k=laptop",
    "monitor": "/s?k=computer+monitor",
    "mouse": "/s?k=computer+mouse",
    "mug": "/s?k=coffee+mug",
    "projector": "/s?k=projector"
}

# User agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
]

# Delay ranges for requests (in seconds)
MIN_DELAY = 2
MAX_DELAY = 5

# Maximum number of images per category
MAX_IMAGES_PER_CATEGORY = 50

# File paths
LOG_FILE = "logs/scraper.log"
DATA_DIR = "data"
