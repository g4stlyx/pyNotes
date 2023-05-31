# -*- coding: utf-8 -*-

import numpy as np

# a = np.arange(1,12,2)
a = np.array([1,3,5,7,9,11])
a = a.reshape(2,3)
print(a)
print(a.dtype) # içerideki elemanların tipini verir
# bir tane bile str varsa hepsini str kabul eder
# aynı şekilde float int'i kapsar (str>float>int)
print(a.ndim)


b = np.array([[1,3],[5,7],[9,11]])
print(b)
print(b.ndim)







