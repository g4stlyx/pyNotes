# -*- coding: utf-8 -*-

import pandas as pd

movies = pd.read_csv("imdb_1000.csv")
movies.columns = ["Oyuncu_oy","İsmi","İçerik oy","Tip","Süre","Oyuncular"]

#print(movies)
#print(movies.columns)
print("************************")
print(movies.head)
print("************************")
print(movies.tail)
print("************************")
print(movies['İsmi'].head())
print("************************")
print(movies[['İsmi','Oyuncu_oy']].head())
print("************************")
print(movies[:10][['İsmi','Oyuncu_oy']].head())


print(movies[
    (movies['Oyuncu_oy']>8.5)&(movies['Oyuncu_oy']<=10.0)]
      [['İsmi','Oyuncu_oy']]) #8.5 10 arasını verir

print(movies[
    (movies['Oyuncu_oy']>8.5)|(movies['Oyuncu_oy']<=10.0)]
      [['İsmi','Oyuncu_oy']]) #8.5'dan büyük ya da 10'dan küçükleri verir

print(movies.query('Oyuncu_oy>=9.0 & Oyuncu_oy<=9.2')
      [['İsmi','Oyuncu_oy']])

