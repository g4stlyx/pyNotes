# -*- coding: utf-8 -*-

import pandas as pd

data1 = {
            'id':[1,2,3,4],
            'ad':["Sefa","Engin","Derin","Salih"],
            'soyad':["Ağardan","Demiroğ","Kaya","Uzun"]
        }

data2 = {
            'id':[1,3,4,7],
            'ad':["Ayşe","Ali","Ahmet","Cemal"],
            'soyad':["Kaya","Kaya","Kaya","Demiroğ"]
        }


data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df)
print(data2Df)
print("**************************")


data3 = pd.merge(data1Df,data2Df,on='id',how='inner')
# aynı id'lileri birleştirir, farklıları yazdırmaz
print(data3)
print("**************************")
data4 = pd.merge(data1Df,data2Df,on='id',how='left')
print(data4)
# solda olup sağda olmayanları da getirir
print("**************************")
data5 = pd.merge(data1Df,data2Df,on='id',how='right')
print(data5)
# sağda olup solda olmayanları da getirir 
print("**************************")

# concat
data6 = pd.concat([data1Df,data2Df],axis=1)
# alt alta yazdırır ; axis=1 yan yana yazdırır
print(data6)








