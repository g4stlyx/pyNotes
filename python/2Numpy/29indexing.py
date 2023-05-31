# -*- coding: utf-8 -*-

import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[5])
print(sayilar[0:3])
print(sayilar[::-1]) # tüm listeyi tersten ver

sayilar2 = np.array([[0,5,10],[15,20,25]])

print(sayilar2[0][0]) # 0. indexin 0. indexini ver
print(sayilar2[:,2]) # her satırdan 2. indexi ver
print(sayilar2[:,0:2]) # her satırın ilk iki elemanını ver

print(sayilar2[-1,:])

