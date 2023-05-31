# -*- coding: utf-8 -*-

# f = open("musteriler.txt","r") # Read def olarak böyle geliyor
# f = open("musteriler.txt","w") # Write koyarak oluşturabiliyoruz
# f = open("musteriler.txt","a") # Append, data ekleme
# f = open("musteriler.txt","x") # Create doysa zaten varsa hata verir
# çoğunlukla "r" kullanılır.

f = open("musteriler.txt")
# print(f.read()) # dosyayı aç 
# print(f.read(10)) # ilk 10 karakteri oku
# print(f.readline()) # satır satır okutur

#%%
print(f.readline())
for l in f:
    print(l)
f.close() # işin bitince dosyayı kapat

#%%
fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("Something") # sth yazar
fileToAppend.write("\n") # boşluk koyar
fileToAppend.close()

#%%
import os
os.remove("ogrenciler.txt") # dosyayı siler

#%%
if os.path.exists("ogrenciler.txt"): # dosya var mı öğrenmek
    os.remove("ogrenciler.txt")
else: 
    print("Böyle bir dosya yok.")
    
#%%
os.rmdir("silinecekKlasor") # klasör siler
