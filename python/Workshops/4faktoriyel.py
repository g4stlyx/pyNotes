# -*- coding: utf-8 -*-

sayi = int(input("Faktöriyeli hesaplanacak sayıyı giriniz."))

faktoriyel = 1

if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz.")
elif sayi==0:
    print("Sonuç: 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
    print("Sonuç : ",faktoriyel)






