import requests
from bs4 import BeautifulSoup

url="https://www.rcpit.ac.in/"
req=requests.get(url)
soup=BeautifulSoup(req.content,"html.parser")
print(soup.prettify())
print(soup.title)


#must install 
# 1. pip install requests
# 2. pip install beautifulsoup4