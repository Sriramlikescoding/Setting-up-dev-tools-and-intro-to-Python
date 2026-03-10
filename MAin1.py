import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
import pandas as pd

data = pd.read_csv("Titanic Dataset.csv")

print(data.head(5))
print(data.isnull().sum())

p.boxplot(data["Age"])
p.title("Age Distribution")
p.show()

p.boxplot(data["Fare"])
p.title("Fare Over Passsengers")
p.show()