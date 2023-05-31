# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv('imdb_1000.csv')

print(films.columns)

films = films.drop('content_rating',axis=1)
films = films.drop('actors_list',axis=1)
films = films.drop(2,axis=0) # 2. satırı siler
#axis=0 satır, axis=1 sütun

rowsToDrop = [0,1,3,4,6,8,9,10] # silinecek satırları listele

films = films.drop(rowsToDrop,axis=0) # listelenenleri sil

print(films)

