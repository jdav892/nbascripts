from selenium.webdriver.common.by import By
from decorators import db_writer
from utils.selenium_setup import create_driver

def scrape_points():
    driver = create_driver()
    try:
        driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
        
        @db_writer("points_per_game")
        def scoring_leader():
            highest_ppg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .who").text
            highest_ppg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .value").text
            return (highest_ppg_name, highest_ppg_value)
        
        return scoring_leader()
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_points()
