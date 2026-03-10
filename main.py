import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
import pandas as pd

data = pd.read_csv("Titanic Dataset.csv")

print(data.head(5))
print(data.isnull().sum())
age_q1 = np.quantile(data["Age"], 0.25)
age_q2 = np.quantile(data["Age"], 0.5)
age_q3 = np.quantile(data["Age"], 0.75)

print("Age quartiles are")
print("Q1 - ", age_q1)
print("Q2 - ", age_q2)
print("Q3 - ", age_q3)


IQR_Age = age_q3 - age_q1
print("Interquartile Range is ", IQR_Age)

#Showing graph

p.hist(data["Age"])
p.xlabel("Age")
p.ylabel("Count of Passengers")
p.show()

#Calculate Quartiles of Fare
Q1_Fare = np.quantile(data["Fare"], 0.25)
Q2_Fare = np.quantile(data["Fare"], 0.5)
Q3_Fare = np.quantile(data["Fare"], 0.75)
IQR_Fare = Q3_Fare-Q1_Fare

print("Quartiles are ", Q1_Fare, Q2_Fare, Q3_Fare)
print("IQR is", IQR_Fare)

p.hist(data["Fare"])
p.xlabel("Fare")
p.ylabel("Count of passengers")
p.show()
