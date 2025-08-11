from selenium.webdriver.common.by import By
from decorators import db_writer
from utils.selenium_setup import create_driver

def scrape_steals():
    driver = create_driver()
    try:
        driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
        print("Scraping steals per game...")
        
        @db_writer("steals_per_game")
        def steal_leader():
            highest_spg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .who").text
            highest_spg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .value").text
            return (highest_spg_name, highest_spg_value)
        
        return steal_leader()
    finally:
        driver.quit()


steal_leader()

driver.quit()
