from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decorators import writer

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
@writer("ppg_leader.text")
def scoring_leader():
    highest_ppg_name = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .who").text
    highest_ppg_value = driver.find_element(By.CSS_SELECTOR, value="#leaders_pts_per_g .first_place .value").text
    return f"{highest_ppg_name}, {highest_ppg_value}"
     
    #with open("ppg_leader.text", "w") as f:
    #    f.write(f"{highest_ppg_name}, {highest_ppg_value}")
#
scoring_leader()
#
#
driver.quit()