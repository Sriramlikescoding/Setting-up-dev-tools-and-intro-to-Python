import pandas as pd
import matplotlib.pyplot as p
import seaborn as sns
import numpy as np

data = pd.read_csv("Titanic Dataset.csv")
print(data.info())
print(data.head(6))
print(data.isnull().sum())
sns.set_style("whitegrid")
sns.countplot(x="Survived", data = data)
p.show()
sns.countplot(x = "Gender", hue = "Survived", data = data)
p.show()
sns.countplot(x = "Gender", hue = "Survived", data = data, palette = "winter" )
p.show()
sns.countplot(x = "Gender", hue = "Embarked", data = data, palette = "winter")
p.show()
sns.countplot(x = "Gender", hue = "Embarked", data = data, palette = "coolwarm")
p.show()
sns.countplot(x = "Gender", hue = "Embarked", data = data, palette = "pastel")
p.show()
sns.countplot(x = "Gender", hue = "Embarked", data = data, palette = "rocket")
p.show()