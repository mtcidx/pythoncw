# TRAINING CLASS : SHAPE
# from shape import Segitiga
# hari = ['Senin', 'Selasa', 'Rabu']
# for h in hari:
#     print(h)

# def hitung_luas_segitiga(alas, tinggi):
#     return alas * tinggi / 2

# print('Segitiga 1', hitung_luas_segitiga(10, 20))

# s1 = Segitiga(10, 20)
# print(s1.hitung_luas_segitiga())
# s2 = Segitiga(40, 50)
# print(s2.hitung_luas_segitiga())

# TRAINING SCRAPPING
from bs4 import BeautifulSoup
import requests
url = 'http://www.detik.com'
page = requests.get(url)
print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
array_p = soup.find_all('p')
print(array_p)
