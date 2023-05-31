# -*- coding: utf-8 -*-

import sys


liste = [7,'engin',0,3,"6"]

for x in liste:
    try: 
        print("Sayı: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç: " + str(sonuc))
    except ValueError:
        print(str(x) + " bir sayı değil.")
        print("Sistem diyor ki:" + str(sys.exc_info()[0]))
    except ZeroDivisionError:
        print(str(x) + "için 0'a bölünme hatası.")
        print("Sistem diyor ki:" + str(sys.exc_info()[0]))
    except:
        print("Başka bir hata oluştu.")
        print("Sistem diyor ki:" + str(sys.exc_info()[0]))
    finally:
        print("İşlemler bitti.")

