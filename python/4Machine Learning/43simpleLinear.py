# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 



data = pd.read_csv("hw_25000.csv")

boy = data.Height.values.reshape(-1,1)
kilo = data.Weight.values.reshape(-1,1)

regression = LinearRegression()
regression.fit(boy,kilo)
print(regression.predict(np.array([[71]]))) # boyu 71 olanın kilosunu tahmin eder


# ***************************************************


print(data.columns)

plt.scatter(data.Height,data.Weight) # resimleştirir
x = np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,regression.predict(x),color="red")
# x,y(x'in tahmini karşılığı) olacak şekilde çizgi çizer
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Simple Linear Regression Model")
plt.show()

print(r2_score(kilo,regression.predict(boy)))
# sapma oranı nedir onun skorunu verir
# burada %25 doğru çıkıyor örneğin

