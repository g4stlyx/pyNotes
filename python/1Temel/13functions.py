# -*- coding: utf-8 -*-

# %%
city = "Ankara"

print(city.upper()) # şehri büyük harfle yaz
print(city.endswith("a")) # şehir a ile'mi bitiyor

# %%
def selamVer(isim = "Ziyaretçi"):
    print("Selam " + isim)
    
selamVer()
selamVer("Ahmet")
selamVer("Mehmet")

# %%
def selamVer2(isim = "Ziyaretçi", soyIsim = "arkadaş"):
    print("Selam " + isim + " " + soyIsim)

selamVer2()
selamVer2("Ahmet")
selamVer2("Ahmet","Kaya")

# %% return'lü fonksiyonlar

def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(5,10)

print(alan)

# %% tek satırlık return'lü fonksiyonlar

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlaniHesapla2(5,20))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2
print(x(4,5))

