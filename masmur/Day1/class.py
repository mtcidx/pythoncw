# nama class awalan huruf besar
class Segitiga:
    def __init__(self):
        self.alas = 0
        self.tinggi = 10

s1 = Segitiga()
print(s1.alas)

s2 = Segitiga()
print(s2.tinggi)



class Segitiga2:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return self.alas * self.tinggi / 2
        

s1 = Segitiga2(10,5)
print(s1.alas)

s2 = Segitiga2(80, 7)
print(s2.tinggi)
print(s2.hitung_luas())