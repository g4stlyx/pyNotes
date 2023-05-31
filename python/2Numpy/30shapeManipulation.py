# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.shape)

a = a.ravel() #shape'i dümdüz bir listeye çevirir(1,x)
print(a)
print(a.shape) # hangi şekilde olduğunu verir

a = a.reshape(2,6) # yeniden şekillendirir
print(a)
print(a.T) #2,6 yı 6,2 yapar, yana çevirmiş gibi oluyor
print(a.reshape(2,-1)) #2 satır oluştur,2 satırı oto parçala

