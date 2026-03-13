import pandas as pd
import matplotlib.pyplot as p
import seaborn as sns
import numpy as np

data = pd.read_csv("Titanic Dataset.csv")
print(data.info())
print(data.head(6))
print(data.isnull().sum())

nominal_category = ["Name", "Ticket", "Cabin"]
ordinal_category = ["Embarked", "Gender"]

print(data["Gender"].value_counts())
gender_category = ["female", "male"]
data["Gender"] = pd.Categorical(data["Gender"], gender_category, ordered = True)
median_index = np.median(data["Gender"].cat.codes )
median_gender = gender_category[int(median_index)]
print(f"Median Gneder is {median_index}")

print(data["Embarked"].value_counts())
embarked_categories = ["S", "C", "Q"]
data["Embarked"] = pd.Categorical(data["Embarked"], embarked_categories, ordered = True)
embarked_index = np.median(data["Embarked"].cat.codes)
median_embarked = embarked_categories[int(embarked_index)]
print(f"Median Embarked is {median_embarked}")
