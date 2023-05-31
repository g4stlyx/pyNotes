# en çok bunlarla çalışılacak

import pandas as pd

data = [10,20,30,40,50]
df = pd.DataFrame()
print(df)

print("*************")
data2 = [["Engin",33,"Ankara"],["Sefa",18,"İstanbul"],["Derin",4,"Ankara"]]
df2 = pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"],index=["index1","index2","index3"])
print(df2)

print("*************")
data3 = {"İsim":["Engin","Sefa","Derin"],"Yaş":[32,18,4],"Şehir":["Ankara","İstanbul","Ankara"]}
df3 = pd.DataFrame(data3,columns=["İsim","Yaş","Şehir"],index=["index1","index2","index3"])
print(df3)
print("*************")
print(df3["Yaş"])
print("*************")
# del df3["Şehir"] #şehir kolonunu uçurur
# df3.pop("Şehir")
# print(df3)

print(df3.loc["index2"]) # 2. kişinin bilgilerini verir
print("*************")
print(df3.iloc[0]) # ilk kişiyi verir
print("*************")

df4 = df3.append(df2) # 3'ü 2 ile birleştirdi.
print(df4)
print("*************")
print(df4.head()) # en tepedeki 5 veriyi verir.
print("*************")
print(df4.tail()) # en alttaki 5 veriyi verir.
print("*************")





