# -*- coding: utf-8 -*-

# ogrenci1 = "Engin"
# ogrenci2 = "Salih"
# ogrenci3 = "Derin"

ogrenciler = ["Engin","Derin","Salih"]

ogrenciler.append("Ahmet") # ekle ve kaldır 
ogrenciler.remove("Salih")

print(ogrenciler)

# list constructor
sehirler = list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

#other functions

# print(sehirler.clear())
print("Ankara sayısı =" + str(sehirler.count("Ankara")))
print("Ankara indexi =" + str(sehirler.index("Ankara")))
sehirler.pop(1) # 1'i çıkartır
sehirler.insert(0,"İstanbul") # 0'a ist. ekler
sehirler.reverse() # ist ank ank => ank ank ist
print(sehirler)


sehirler3 = sehirler.copy()
sehirler2 = sehirler

sehirler2[0]="İzmir"
print(sehirler)
print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3) # sehirlere sehirler3'ü ekler
print(sehirler)

sehirler.sort() # sehirler'i a'dan z'ye sıralar
print(sehirler)

