from shape import Rectangle, Triangle
import requests

if __name__ == "__main__":
	alas = int(input("masukan alas: "))
	tinggi = int(input("masukan tinggi: "))
	rect = Rectangle(alas, tinggi)
	trian = Triangle(alas, tinggi)
	print(rect.luas)
	print(trian.luas)
	req = requests.get('http://kjasdfkhsajkdhfkjsdhvkndsjnvio.com/')
	print(req.status_code)
	
	