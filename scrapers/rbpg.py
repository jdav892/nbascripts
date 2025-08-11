from selenium.webdriver.common.by import By
from decorators import db_writer
from utils.selenium_setup import create_driver

def scrape_rebounds():
    driver = create_driver()
    try:
        driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
        print("Scraping rebounds per game...")
        
        @db_writer("rebounds_per_game")
        def rebound_leader():
            highest_rbpg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_trb_per_g .first_place .who").text
            highest_rbpg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_trb_per_g .first_place .value").text
            return (highest_rbpg_name, highest_rbpg_value)
        
        return rebound_leader()
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_rebounds()
