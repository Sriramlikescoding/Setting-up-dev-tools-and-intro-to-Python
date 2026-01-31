import matplotlib.pyplot as p
import pandas as pd
import numpy as np
import seaborn as sns
import warnings

df = pd.read_csv("Heart.csv")
df.head()
print(df.head())
df.shape
print(df.shape)
df.columns
print(df.columns)
df.describe()
print(df.describe())
df.isnull().sum()
print(df.isnull().sum())
print(df.info())
df.hist(figsize=(12,12),layout=(5,3))
df.plot(kind="box",subplots=True, layout=(5,3), figsize=(12,12))
p.figure(figsize=(6,4))
sns.barplot(data=df,x="sex",y="chol",hue="target",palette="spring")
p.show()
print("sex value counts")
print(df["sex"].value_counts())
print("Target Value Counts")
print(df["target"].value_counts())
p.figure(figsize=(20,10))
sns.heatmap(df.corr(),annot=True, cmap="terrain")
p.show()