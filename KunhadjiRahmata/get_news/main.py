import bs4
import requests

r = requests.get('http://www.detik.com')
html = bs4.BeautifulSoup(r.text, features="html.parser")
print(html.title.text)