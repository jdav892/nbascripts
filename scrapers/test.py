from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date as dt

today = dt.today()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")

def scoring_leader():
    highest_ppg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .who").text
    highest_ppg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .value").text
    print (f"{highest_ppg_name}, {highest_ppg_value}, {today}")


def assist_leader():
    highest_apg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .who").text
    highest_apg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .value").text
    print (f"{highest_apg_name}, {highest_apg_value}, {today}")


def rebounding_leader():
    highest_rbpg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_trb_per_g .first_place .who").text
    highest_rbpg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_trb_per_g .first_place .value").text
    print (f"{highest_rbpg_name}, {highest_rbpg_value}, {today}")

def block_leader():
    highest_bpg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .who").text
    highest_bpg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .value").text
    print (f"{highest_bpg_name}, {highest_bpg_value}, {today}")


def steal_leader():
    highest_spg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .who").text
    highest_spg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .value").text
    print (f"{highest_spg_name}, {highest_spg_value}, {today}")






def initializer():
    print("Scraping In Progress")
    scoring_leader()
    assist_leader()
    block_leader()
    rebounding_leader()
    steal_leader()
    print("Scraping Complete")


initializer()

driver.quit()
