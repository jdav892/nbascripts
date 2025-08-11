from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    """Get Chrome options based on configuration"""
    config = get_config()
    selenium_config = config.get('selenium', {})
    
    options = Options()
    
    if selenium_config.get('headless', True):
        options.add_argument('--headless')
    
    if user_agent := selenium_config.get('user_agent'):
        options.add_argument(f'user-agent={user_agent}')
    
    # Add additional Chrome options for stability in Docker
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    return options

def create_driver():
    """Create a new Chrome driver with configured options"""
    config = get_config()
    selenium_config = config.get('selenium', {})
    
    options = get_chrome_options()
    driver = webdriver.Chrome(options=options)
    
    # Set timeout from config
    if timeout := selenium_config.get('timeout_seconds'):
        driver.implicitly_wait(timeout)
    
    return driver
