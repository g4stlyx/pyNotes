# -*- coding: utf-8 -*-

def topla(sayi1,sayi2):
    print(int(sayi1) + int(sayi2))
def cikar(sayi1,sayi2):
    print(int(sayi1) - int(sayi2))
def carp(sayi1,sayi2):
    print(int(sayi1) * int(sayi2))  
def bol(sayi1,sayi2):
    print(int(sayi1) / int(sayi2))

print("1 : Topla")
print("2 : Çıkar")
print("3 : Çarp")
print("4 : Böl")
secenek = input("Yapmak istediğiniz işlemin numarasını yazınız:")

sayi1 = input("1. sayıyı giriniz.")
sayi2 = input("2. sayıyı giriniz.")
        

if secenek == "1" :
    topla(sayi1,sayi2)
elif secenek == "2" :
    cikar(sayi1,sayi2)
elif secenek == "3" :
    carp(sayi1,sayi2)
elif secenek == "4" :
    bol(sayi1,sayi2)
else:
    print("Lütfen geçerli bir işlem numarası giriniz.-1,2,3,4-")
    
