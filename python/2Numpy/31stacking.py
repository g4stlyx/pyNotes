# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))
print(a)
print(b)

c = np.vstack((a,b)) # iki diziyi alt alta koyup birleştirir
print(c) # sütun sayısı aynı

d = np.hstack((a,b)) # iki diziyi yan yana koyup birleştirir
print(d) # satır sayısı aynı





