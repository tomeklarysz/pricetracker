import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,,0,,,,8143O1777802/1/')
soup = BeautifulSoup(r.content, features="lxml")

links = []
titles = []
prices = []

for link in soup.find_all('a', class_='productLink'):
    if "https://www.morele.net"+link.get('href') not in links:
        links.append("https://www.morele.net"+link.get('href'))
    
    if link.get('title') not in titles:
        titles.append(link.get('title'))


for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(class_="product-price").get_text().strip()
