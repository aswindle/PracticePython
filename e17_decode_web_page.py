import requests

r2 = requests.get('http://www.politico.com/index.html').text
r3 = r2.encode('ascii', 'ignore')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r3, "html.parser")

for link in soup.find_all(class_="headline-list"):
    print(link.text)