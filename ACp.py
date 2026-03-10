import matplotlib.pyplot as p
import pandas as pd
import seaborn as sns
import numpy as np

data = pd.read_csv("Bestsellers with categories.csv")

print(data.info())
print(data.head(6))
print(data.isnull().any())
print(data.isnull().sum())

Std = np.std(data["User Rating"])
print(Std)

Variance = np.var(data["User Rating"])
print(Variance*10)

p.hist(data["User Rating"])
p.show()