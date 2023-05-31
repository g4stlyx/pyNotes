# -*- coding: utf-8 -*-

import pandas as pd

url = "https://bit.ly/uforeports"

data = pd.read_csv(url)
#%%
print(data)
print(data.columns)
print(data[["City","Colors Reported","Shape Reported",
            "State","Time"
            ]].head())

print(data.isnull().head(100)) # data boş mu
print(data.notnull().head(100)) # data dolu mu
print(data.isnull().sum()) # kaç tane boş bilgi var
print(data[data.City.isnull()])



#%%
# dropna *************************************

print(data.shape)
# data = data.dropna(how = "any") 
# any >>> 1+ boşluklu/nanlı dataları siler
# all >>> hepsi boş dataları siler
data = data.dropna(
    subset=['City','Colors Reported'],how = 'all')
# all ikisi de boşsa siler, any biri bile boşsa siler
print(data.shape)



#%%
# fillna *************************************


data['Shape Reported'].fillna(value=
                              'Belirsiz',inplace=True)
print(data['Shape Reported'].value_counts(dropna=False))
print(data.shape)

# Nan-boş-girilmemiş değerleri belirsiz olarak değiştirir




