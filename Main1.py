import matplotlib.pyplot as p
import pandas as pd
import seaborn as sns
import numpy as np

data = pd.read_csv("Movie.csv")

print(data.info())
print(data.head(6))
print(data.isnull().any())
print(data.isnull().sum())
p.hist(data["Runtime"])
p.xlabel("Movie Rating")
p.ylabel("Count of Movies")
p.show()
data["Runtime"].unique()
bins = np.arange(80,230,10)
p.hist(data["Runtime"], edgecolor = "black", bins=bins, color = "g")
p.xlabel("Movie Count")
p.ylabel("Count of Movies")
p.show()
data["IMDB_Rating"].unique()
bins = np.arange(8,10,0.20)
p.hist(data["IMDB_Rating"], edgecolor = "black", bins = bins, color = "r")
p.ylabel("Movie Countt")
p.xlabel("Imdb Rating")
p.xticks(bins)
p.show()