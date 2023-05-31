# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN",
                  "Test1","Test2","Test3","Test4","Final","Not"]

print(notlar)
print(notlar.loc[:,"İsim"])
print("*****************")
print(notlar.loc[:5,"İsim"]) # pandas'da 5 de dahil
print("*****************")
print(notlar.loc[:5,"İsim":"SSN"]) # isimden ssn'e kadar verir
print("*****************")
print(notlar.loc[:5,["İsim","Soyisim","Final"]])
print("*****************")
print(notlar.loc[:5,:"SSN"])
print("*****************")
print(notlar.loc[::-1,:"İsim"]) #Sondan başa isimler
print("*****************")




