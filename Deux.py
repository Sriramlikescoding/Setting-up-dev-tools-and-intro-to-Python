import matplotlib.pyplot as p
import seaborn as s
import pandas as pd
import numpy as np
import warnings

df = pd.read_csv("Penguins.csv")
df.isnull().sum()
print(df.isnull().sum)  
s.heatmap(df.corr(),annot=True, cmap="terrain")







