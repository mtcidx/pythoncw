class Rectangle:
	def __init__(self, alas, tinggi):
		self.alas = alas
		self.tinggi = tinggi
		self.luas = alas*tinggi
	
class Triangle(Rectangle):
	def __init__(self, alas, tinggi):
		self.luas = alas*tinggi/2

