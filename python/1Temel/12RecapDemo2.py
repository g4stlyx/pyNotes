# -*- coding: utf-8 -*-

sayi = int(input("Sayı giriniz : "))
asalMi = True
# print(7 % 2) # 7'nin 2'ye bölümünden kalanı verir.

for x in range(2,sayi):
    if sayi % x == 0 :
        asalMi = False
        break


if asalMi == True :
    print("ASAL")
else:
    print("ASAL DEĞİL")

