# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures


data = pd.read_csv("positions.csv")
print(data.columns)

level = data.iloc[:,1].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = DecisionTreeRegressor()
regression.fit(level,salary)

print(regression.predict(np.array([[8.3]]))) # direkt 8'i verdi
print(regression.predict(np.array([[8.6]]))) # direkt 9'u verdi


plt.scatter(level,salary,color="red")
x = np.arange(min(level),max(level),0.01).reshape(-1,1)
plt.plot(x,regression.predict(x),color="orange")
plt.xlabel("level")
plt.ylabel("salary")
plt.title("Decision Tree Model")
plt.show()



