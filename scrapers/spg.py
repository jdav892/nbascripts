from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decorators import writer

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.basketball-reference.com/leagues/NBA_2025_leaders.html")
#TODO: store print values in variables to write to text file to plot data points later

print("Scraping in Progress")
@writer("spg_leader.csv")
def steal_leader():
    highest_spg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .who").text
    highest_spg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_stl_per_g .first_place .value").text
    return f"{highest_spg_name, highest_spg_value}"


steal_leader()

driver.quit()