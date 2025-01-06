from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
""" TODO: Rewrite this Selenium crawler to click on each player's profile,
and select out the img element for each league leader so I will have an img
to display with the static data that beautiful soup scrapes.
"""
#point_search = driver.find_element(By.CSS_SELECTOR, value="div table tbody .text-right")
#print(point_search.text)


#TODO: store print values in variables to write to text file to plot data points later
print("Scraping in Progress")
def scoring_leader():
    highest_ppg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .who").text
    highest_ppg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .value").text
    
    
def rebounding_leader():
    highest_trbpg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_trb_per_g .first_place .who").text
    highest_trbpg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_trb_per_g .first_place .value").text
    print(highest_trbpg_name, highest_trbpg_value)
    
def assist_leader():
    highest_apg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .who").text
    highest_apg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .value").text
    print(highest_apg_name, highest_apg_value)
    
def steal_leader():
    highest_stl_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .who").text
    highest_stl_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .value").text
    print(highest_stl_name, highest_stl_value)
    
def block_leader():
    highest_blk_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .who").text
    highest_blk_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .value").text
    print(highest_blk_name, highest_blk_value)
    
scoring_leader()
rebounding_leader()
assist_leader()
steal_leader()
block_leader()

driver.quit()

if __name__ == "__main__":
    print("Scrape Complete")

