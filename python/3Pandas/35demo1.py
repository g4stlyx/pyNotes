# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN",
                  "Test1","Test2","Test3","Test4","Final","Not"]

print(notlar)
print(type(notlar))
print("**********")
print(notlar.head()) # ilk 5 data
print("**********")
print(notlar.tail()) # son 5 data
print("**********")

print(notlar["İsim"])
print("**********")
print(notlar["Soyisim"])
print("**********")
print(notlar.iloc[2])
print("**********")
print(notlar[0:10])

