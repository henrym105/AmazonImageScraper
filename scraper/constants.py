# Base URL and category paths
AMAZON_BASE_URL = "https://www.amazon.com"
CATEGORIES = {
    "electronics": "/s?k=electronics",
    "books": "/s?k=books",
    "fashion": "/s?k=fashion",
    "home_kitchen": "/s?k=home+and+kitchen",
    "toys_games": "/s?k=toys+and+games",
    "sports_outdoors": "/s?k=sports+and+outdoors",
    "beauty": "/s?k=beauty",
    "automotive": "/s?k=automotive",
    "pet_supplies": "/s?k=pet+supplies",
    "office_products": "/s?k=office+products"
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
