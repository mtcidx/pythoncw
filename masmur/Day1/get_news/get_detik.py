import requests
import bs4

r = requests.get('http://www.detik.com')
# cek status , jika hasilnya 200 maka berhasil
print(r.status_code) 

# cetak isinya
html = bs4.BeautifulSoup(r.text, features="html.parser")
print(html.title.text)