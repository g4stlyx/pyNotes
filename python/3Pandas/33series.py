# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = np.array(["Engin","Derin","Salih"])
s = pd.Series(data, index=[1,2,3])
print(s)
print(s[1])

print("***************************")

data2 = {"mat":10, "fiz":20,"beden":100}
s2 = pd.Series(data2, index= ["fiz","mat","beden"])
print(s2)
print(s2[0])
print(s2["beden"])

print("***************************")

s3 = pd.Series(5,index=[1,2,3,4,5])
print(s3)







