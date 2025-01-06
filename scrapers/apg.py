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
@writer("apg_leader.csv")
def assist_leader():
    highest_apg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .who").text
    highest_apg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_ast_per_g .first_place .value").text
    return f"{highest_apg_name}, {highest_apg_value}"


assist_leader()

driver.quit()