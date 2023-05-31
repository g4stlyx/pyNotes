# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)
print(a)

b = a
print(b)
print(a[2])
print(b[2])
b[0] = 100
print(a)
print(b)  # b değişince a da değişti

c = a.copy()
c[0] = 1000
print(a)
print(c) # c değişmesine rağmen a aynı

d= a.view()
print("*******")
print(a)
print(d)
d[0] = 250
print(a) # d değişince a da değişti
print(d) 

d.shape = 2,5

print(a) # ama şekli değişmedi
print(d)

#yani view'de data hep aynıdır fakat şekil farklı olabilir