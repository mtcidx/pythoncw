import requests
import bs4

r = requests.get('https://www.detik.com')
html = bs4.BeautifulSoup(r.text, features="html.parser")
print(html.title.text)