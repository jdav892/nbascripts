from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt

 
URL = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html#per_game_stats::pts_per_g"
 
response = requests.get(URL)
url_page = response.text

soup = BeautifulSoup(url_page, "html.parser")


ppg_list_left = soup.find_all(attrs="tbody", class_="first_place")

ppg_list_right = soup.find_all(attrs="tbody", class_="first_place")

print(ppg_list_left)
print(ppg_list_right)
print(dt.today())