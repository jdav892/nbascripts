from selenium.webdriver.common.by import By
from decorators import db_writer
from utils.selenium_setup import create_driver

def scrape_blocks():
    driver = create_driver()
    try:
        driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
        
        @db_writer("blocks_per_game")
        def block_leader():
            highest_bpg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .who").text
            highest_bpg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .value").text
            return (highest_bpg_name, highest_bpg_value)
        
        return block_leader()
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_blocks()
