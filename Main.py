import numpy as np
import matplotlib.pyplot as p
import seaborn as sns
import pandas as pd

data = pd.read_csv("FuelConsumption.csv")
#Reading data
print(data.isnull().any())
#Checking for null values
figure = p.figure(figsize=(6,4))
sns.scatterplot(data=data, x="FUELCONSUMPTION_COMB", y="CO2EMISSIONS")
sns.scatterplot(data=data, x=)
p.show()