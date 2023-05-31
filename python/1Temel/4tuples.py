# -*- coding: utf-8 -*-

tupleListe = (2,4,6,"Ankara",(1,2,3),[1,2,3])

liste = [2,4,6,"Ankara",[1,2,3],(1,2,3)]

liste[0] = 6
# tupleListe[0] = 6  tuple'ın elemanları değiştirilemez


tupleDeger =("Engin",)
print(tupleDeger)
print(type(tupleDeger))

print(tupleListe[-2])
print(liste[-2])

print(tupleListe[1:2])
print(liste[1:2])

print(tupleListe)
print(liste)

print(len(tupleListe))
print(len(liste))

