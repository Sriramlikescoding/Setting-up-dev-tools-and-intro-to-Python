import pandas as pd
import matplotlib.pyplot as p
import seaborn as sns
import numpy as np

data = pd.read_csv("Titanic Dataset.csv")
print(data.info())
print(data.head(6))
print(data.isnull().sum())

num_data = data.drop(["Name", "Ticket", "Cabin", "Embarked", "Gender"], axis = 1)
labels = ["PassengerId", "Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]

for l in labels:
    p.boxplot(num_data[l])
    print("Distribution of ", l)
    p.show()
