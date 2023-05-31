# -*- coding: utf-8 -*-

print("Birbirine eşit olmayan 3 tam sayı giriniz.")
sayi1 = int(input("Sayı 1'i giriniz."))
sayi2 = int(input("Sayı 2'yi giriniz."))
sayi3 = int(input("Sayı 3'ü giriniz."))

if sayi1 > sayi2 and sayi1 > sayi3:
    print("Sayı 1 en büyük sayıdır.")
    
if sayi2 > sayi1 and sayi2 > sayi3:
    print("Sayı 2 en büyük sayıdır.")
    
if sayi3 > sayi1 and sayi3 > sayi2:
    print("Sayı 3 en büyük sayıdır.")  
    
else:
    print("Sayılar birbirine eşit olmamalı.")