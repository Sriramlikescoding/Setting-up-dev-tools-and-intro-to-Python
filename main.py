import matplotlib.pyplot as p
import pandas as pd
import seaborn as sns
import numpy as np

Data = pd.read_csv("Life_Expectancy.csv")
print(Data.head())
print(Data.info())
grouped_data = Data.groupby("continent").mean(numeric_only=True )
grouped_data = grouped_data.reset_index()
plot = sns.barplot(x = grouped_data["continent"], y=grouped_data["life_exp"], color = "red")
for bar in plot.patches:
    plot.annotate(format(bar.get_height(), ".2f"), (bar.get_x()+bar.get_width()/2, bar.get_height()), ha = "center", va = "center", size = 12, xytext = (0,1), textcoords = "offset points")

p.xlabel("continent", size = 14)
p.ylabel("life_exp", size = 14 )
p.title("annotated barplot")
p.show()
