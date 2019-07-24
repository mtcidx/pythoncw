"""
Keterangan
- sequential
- brancing
- loop
"""
from shape.bujursangkar import Bujursangkar
from shape.segitiga import Segitiga

print('Hello World')
alas = 500
tinggi = 2
luas_segitiga = alas * tinggi / 2
print (luas_segitiga)

# brancing dengan if

if luas_segitiga < 100:
    print('kecil')
elif luas_segitiga < 20 and luas_segitiga < 50:
    print('Menengah')
else:
    print('besar')

# loop dengan jumlah yang pasti
for i in range(0, 11):
    print(i)

# array
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

for h in hari:
    print(h)

jumlah_bilang = 5
while jumlah_bilang > 0:
    print (jumlah_bilang)
    jumlah_bilang = jumlah_bilang - 1


# modularisasi and function

def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2


segitiga1 = hitung_luas_segitiga(100, 3)
print('segitiga1', segitiga1)
print ('segitga2 ', hitung_luas_segitiga(20, 10))

# class Segitiga:
#     def __init__(self, alas, tinggi):
#         self.alas = alas
#         self.tinggi = tinggi
#     def hitung_luas(self):
#         return self.alas * self.tinggi/2

s1 = Segitiga(100, 20)
print(s1.alas)

s2 = Segitiga(8, 9)
print(s2.tinggi)

b1 = Bujursangkar(5, 4)
print(b1.panjang)
