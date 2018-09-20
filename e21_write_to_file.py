import requests
from bs4 import BeautifulSoup

article = requests.get('http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture').text.encode('utf16', 'ignore')
soup = BeautifulSoup(article, 'html.parser')
filename = input("Enter a filename: ")
with open(filename + '.txt', 'w') as open_file:
    for paragraph in soup.find_all('p'):
        open_file.write('\n' + "     " + paragraph.text)
