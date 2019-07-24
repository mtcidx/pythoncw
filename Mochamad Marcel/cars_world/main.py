"""
keterangan: sintaksis dasar
-sequntial
-brancing
-loop
"""
from shape.persegi_panjang import Persegi_panjang
from shape.segitiga import Segitiga

print('hello,world!')
alas = 40
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

# branching dengan if
if luas_segitiga < 20:
    print('Kecil')
elif luas_segitiga > 20 and luas_segitiga < 50:
    print('Menengah')
else:
    print('Besar')

# loop dengan jumlah loop yang pasti
for i in range(0, 11):
    print(i)

# loop untuk list
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
for h in hari:
    print(h)

jumlah_bilangan = 5
while jumlah_bilangan > 0:
    print(jumlah_bilangan)
    jumlah_bilangan = jumlah_bilangan - 1


# Modularisation with function
def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi / 2


segitiga1 = hitung_luas_segitiga(10, 3)
print('Segitiga 1 =', segitiga1)
print('Segitiga 2 =', hitung_luas_segitiga(90, 6))




s1 = Segitiga(10, 5)
print(s1.hitung_luas())

s2 = Segitiga(80, 7)
print(s2.hitung_luas())

p1 = Persegi_panjang(10, 5)
print(p1.hitung_luas())
