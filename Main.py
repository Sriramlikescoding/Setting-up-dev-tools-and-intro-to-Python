import pandas as pd
import matplotlib.pyplot as p
import numpy as np
import seaborn as sns

data = pd.read_csv("Data.csv")
print(data.head())
print(data.info())
print(data.isnull().any())
labels = ["population", 'life_exp', "gdp_cap"]
#Columns that we picked.
for i in labels:
    sns.boxplot(y=data[i], palette="winter")
    #Shows data for each column
    p.show()
sns.boxplot(y = "gdp_cap", x = "continent", data=data, palette="viridis")
p.show()
sns.boxplot(y="life_exp", x="continent", data=data, palette="viridis")
p.show()
sns.violinplot(y="gdp_cap", x="continent", data=data, palette="bright")
p.show()
sns.violinplot(y="life_exp", x="continent", data=data, palette="viridis")
#Looks like violin
p.show()
for i in labels:
    sns.kdeplot(data[i])
    #Wavey plot shows data over time
    p.show()
for i in labels:
    p.hist(data[i])
    p.xlabel(i)
    p.show()
for i in labels:
    sns.distplot(data[i])
    p.show()
    print(f"skewness is", data[i].skew())
    #If skewness = 0, graph is symmetric, curve is in center
    #If skewness > 0, graph is towards right, curve is on right
    #If skewness < 0 graph is towards left, curve is on left
