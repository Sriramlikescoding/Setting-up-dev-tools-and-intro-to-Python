import matplotlib.pyplot as p
import pandas as pd
import seaborn as sns
import numpy as np

Data = pd.read_csv("Life_Expectancy.csv")

grouped_data = Data.groupby("continent").mean(numeric_only=True)
grouped_data = Data.reset_index()

plot = sns.barplot(x = grouped_data["continent"], y = grouped_data["gdp_cap"], palette="winter")
for bar in plot.patches:
    plot.annotate(format(bar.get_height(), ".2f"), (bar.get_x()+bar.get_width()/2, bar.get_height()), ha = "center", va = "center", size = 12, xytext = (0,1), textcoords = "offset points")

p.xlabel("continent")
p.ylabel("gdp_cap")
p.title("Annotated graph")
p.show()