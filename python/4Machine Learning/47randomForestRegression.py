# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# ensemble = aynı algoritmayı tekrar tekrar gerçekleştirir.

data = pd.read_csv("positions.csv")
level = data.iloc[:,1].values.reshape(-1,1)
salary= data.iloc[:,2].values

regression = RandomForestRegressor(n_estimators=100, random_state=0)
# kaç tane decision tree kurduğunu girdik
# random state sonucun değiştirilmeyeceğini anlatır
regression.fit(level,salary)

print(regression.predict(np.array([[8.3]])))




