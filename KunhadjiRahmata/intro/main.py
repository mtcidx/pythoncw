"""
keterangan siktaksis dasar
-squential
-branching dengan if
-loop
"""
from shape.persegi import Persegi
from shape.segitiga import Segitiga

print('hello world!')

# Sequential
print('contoh luas segitiga')
alas = 400
tinggi = 3
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

# branching dengan if
print('branching dengan if')
if luas_segitiga < 100:
    print('kecil')
elif luas_segitiga > 100 and luas_segitiga < 700:
    print('Menengah')
else:
    print('besar')
# loop
print('loop')
for i in range(0, 10):
    print(i + 1)

# loo[ untuk list
print('loop untuk list')
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum''at', 'Sabtu', 'Minggu']
for h in hari:
    print(h)

# loop untuk while
jumlah_bilang = 5
while jumlah_bilang > 0:
    print(jumlah_bilang)
    jumlah_bilang = jumlah_bilang - 1

# modularisasi dengan function
print('modularisasi dengan function')


def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2


segitiga1 = hitung_luas_segitiga(10, 3)
print('segitiga 1', segitiga1)
print('segitiga 2', hitung_luas_segitiga(90, 6))

s1 = Segitiga(10, 5)
print(s1.hitung_luas())

s2 = Segitiga(80, 7)
print(s2.hitung_luas())

p1 = Persegi(20, 20)
print(p1.hitung_luas())

p2 = Persegi(4, 9)
print(p2.hitung_luas())