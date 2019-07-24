import requests
import bs4

r = requests.get('http://www.detik.com')
r.status_code
#print(r.status_code)
#print(r.text)

html = bs4.BeautifulSoup(r.text, features="html.parser")
print(html.title.text)