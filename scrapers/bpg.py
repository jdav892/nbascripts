from selenium import webdriver
from selenium.webdriver.common.by import By
from decorators import writer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")

print("Scraping in Progress")
@writer("bpg_leader.csv")
def block_leader():
    highest_bpg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .who").text
    highest_bpg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_blk_per_g .first_place .value").text
    return f"{highest_bpg_name}, {highest_bpg_value}"


block_leader()

driver.quit()
