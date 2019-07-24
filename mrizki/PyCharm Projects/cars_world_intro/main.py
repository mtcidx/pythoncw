from shape.persegi import Persegi
from shape.segitiga import Segitiga

print('Hello World!')
alas = 50
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

if luas_segitiga < 20:
    print('Kecil')
elif luas_segitiga > 20 and luas_segitiga < 50:
    print('Sedang')
else:
    print('Besar')

# loop dengan jumlah yang pasti
for i in range(0, 10):
    print(i)

# loop untuk list
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
for h in hari:
    print(h)

jumlah_bilangan = 5
while jumlah_bilangan > 0:
    print(jumlah_bilangan)
    jumlah_bilangan = jumlah_bilangan - 1

# Function


def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2


segitiga1 = hitung_luas_segitiga(10, 3)
print('segitiga 1', segitiga1)
print('segitiga 2', hitung_luas_segitiga(90, 6))


s1 = Segitiga(10, 5)
print(s1.alas)

s2 = Segitiga(80, 7)
print(s2.tinggi)

Persegii = Persegi(10, 10)
print('Luas Persegi =', Persegii.hitung_luas())

p1 = Persegi(2, 5)
print(p1.panjang)

p2 = Persegi(10, 8)
print(p2.lebar)