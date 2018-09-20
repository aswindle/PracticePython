from bs4 import BeautifulSoup
import requests


article = requests.get('http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture').text.encode('utf16', 'ignore')
soup = BeautifulSoup(article, 'html.parser')

for paragraph in soup.find_all('p'):
    print(paragraph.text)
