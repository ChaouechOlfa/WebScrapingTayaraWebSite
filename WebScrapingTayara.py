import requests
import time
import csv
import re
from bs4 import BeautifulSoup
from itertools import zip_longest
articles =[]
links= []
base_url = "https://www.tayara.tn/"
url = "https://www.tayara.tn/fr/ads/c/V%C3%A9hicules/?page=1"
result = requests.get(url)
src = result.text
#print(src)
soup = BeautifulSoup(src, "html.parser")
blocks = soup.find_all('article', class_ ="mx-0")
print(blocks)
for block in blocks:
    articles = block.find_all('a', target='_blank')
# Afficher les liens pour chaque bloc
    for article in articles:
        href = article.get('href')
        if href:
            print(base_url+href)



