from selenium import webdriver
from decorators import db_writer 
from utils.selenium_setup import create_driver

def scrape_assists():
    driver = create_driver()
    try:
        driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
    
        @db_writer("assister_per_game")
        def assist_leader():
            highest_apg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .who").text
            highest_apg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .value").text
            return f"{highest_apg_name}, {highest_apg_value}"
    
        return assist_leader()
    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_assists()