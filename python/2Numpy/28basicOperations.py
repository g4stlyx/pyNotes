# -*- coding: utf-8 -*-
#bunları ezbere bilmen gerekmiyor,np ile ne yapabilceğini bil
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

c = a-b #ikisinin de aynı sayıda elemanı olmalı
d = b**3
e = 10 * np.sin(a)


print(a)
print(b)
print(c)
print(d)
print(e)
print(e<7)
print(a*b)
print(a@b) # matris çarpımı 1. yol
print(a.dot(b)) # matris çarpımı 2.yol

f = np.ones((2,4))
g = np.zeros((2,4))
h = np.random.random((2,4)) # 0-1 arası rastgele sayılar verir
i = np.sum(b) # topla
j = np.min(b)
k = np.max(h) 
l = np.sqrt(b) # kareköklerini verir


