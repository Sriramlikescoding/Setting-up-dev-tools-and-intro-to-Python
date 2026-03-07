import matplotlib.pyplot
import pandas as pd
import seaborn as sns
import numpy as np

data = pd.read_csv("Weather Dataset.csv")

print(data.info())
print(data.head(6))
print(data.isnull().any())
print(data.isnull().sum())

mean_temperature = np.mean(data["Temperature (C)"])
print(f"Mean temperature is {mean_temperature}")
variance_temp = np.var(data["Temperature (C)"])
print("Standard deviation is {variance_temp}")
standard_deviation = np.std(data["Temperature (C)"])
print(f"Standard deviation is {standard_deviation}")

for i in range(1,13):
    month = data.loc[data["month"]==i]["Temperature (C)"]
    print(f"Month {str(i)}")
    print(f"Mean Temperature is {str(np.mean(month))}")
    print(f"standard devviation is {str(np.std(month))}")
    

