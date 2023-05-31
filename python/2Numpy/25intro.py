# -*- coding: utf-8 -*-
# listelere benzer bir kütüphane

import numpy as np

a = np.arange(0,16,5).reshape(2,2) # 5'er 5'er 0-15 yazdırır
# 2'şer sayıdan oluşacak şekilde 2 grup oluşturur

print(a)
print(type(a))

b = np.arange(10) # 0-9 yazdırır
print(b)
print(b.shape) # kaç eleman, kaç boyut var onu gösterir
print("Dimension Count= " + str(b.ndim)) #kaç boyut olduğunu gösterir








