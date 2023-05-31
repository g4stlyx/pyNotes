# -*- coding: utf-8 -*-

sayi1 = 10
sayi2 = 20

if sayi1>sayi2:
    print("Sayı 1, Sayı 2'den büyüktür.")
elif sayi1==sayi2:
    print("Sayı 1, Sayı 2'ye eşittir.")
else: 
    print("Sayı 1, Sayı 2'den küçüktür.")
    
#-------------------------------------------------------

lights = ["red","yellow","green"]

currentLight = input("Please choose the color of  the light: red,yellow or green")

if currentLight == "green":
    print("Color of the light is green, go")
elif currentLight == "yellow":
    print("Color of the light is yellow, prepare to go")
elif currentLight == "red":
    print("Color of the light is red,wait the light to become green")
else:
    print("Please write invalid value for the color of light")

