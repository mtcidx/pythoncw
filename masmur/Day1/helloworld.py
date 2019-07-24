"""
    Keterangan : sintaksis dasar
    - sequantial
    - branching dengan if
    - loop
"""
print("Hellow World !!!")
alas = 40
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

# branching dengan if
if luas_segitiga < 20:
    print('Kecil')
elif luas_segitiga >20 and luas_segitiga < 50:
    print('Menengah')
else:
    print('Besar')

# looping
for i in range(0, 11):
    print(i)

# looping untuk list
hari = ['Sening','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
for h in hari:
    print(h)

jumlah_bilangan = 5
while jumlah_bilangan >0:
    print(jumlah_bilangan)
    jumlah_bilangan = jumlah_bilangan - 1
 

# definisi function
def hitung_luas_segitiga(alas, tinggi):
    return alas * tinggi /2

print('Segitiga 1 : ', hitung_luas_segitiga(10,3))
print('Segitiga 2 : ', hitung_luas_segitiga(90,6))
