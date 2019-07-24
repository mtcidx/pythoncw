#dasar
#-sequential
#-branching dengan if
#-loop

from Shape.segitiga import Segitiga
from Shape.persegi_panjang import Persegi_panjang
from Shape.persegi import Persegi

print ('hello world')

alas = 20
tinggi = 2
luas = alas*tinggi / 2

print (luas)


#branding dengan if COndition
if luas < 20 :
    print('Kecil')
elif luas >= 20 and luas <50 :
    print('Menengah')   
else:
    print('Besar')

#for loop

for i in range ( 0 , 11):
    print(i)

#loop array
hari = ("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")

for i in hari:
    print(i)

jml_bilangan = 5
i = 0
while jml_bilangan > 0:
    print(jml_bilangan)
    jml_bilangan = jml_bilangan - 1 


#function
def hitung_luas(alas,tinggi):
    return alas*tinggi / 2

segitiga1 = hitung_luas(10,3)
print ('segitiga1=',segitiga1)

print('segitiga2=', hitung_luas(30,2))


s1 = Segitiga(20,5)
print('s1 alas',s1.hitung_luas())

s2 = Segitiga(50,2)
print('s2 tinggi',s2.hitung_luas())

#hitung class persegi_panjang
pp = Persegi_panjang(50,10)
print('Luas Persegi Panjang =',pp.hitung_luas())

#hitung class persegi
persegi = Persegi(100)
print('Luas Persegi=', persegi.hitung_luas())