import numpy as np
import pandas as pd
import statistics as st

data = pd.read_csv("Bestsellers with categories.csv")
data.head(6)
print(data.isnull().sum())

Mean_price = np.mean(data["Price"])
print(Mean_price)

Median_price = np.median(data["Price"])
print(Median_price)

mode_price = st.mode(data["Price"])
print(mode_price)