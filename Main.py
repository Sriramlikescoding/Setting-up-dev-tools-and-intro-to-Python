import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
missingValues = ["NA", "na", "N/A", "", np.nan]
df = pd.read_csv("Data.csv", na_values=missingValues)
print(df)
print("Missing_Values Count by Column")
print(df.isnull().sum())
print("Is There Any Missing Values")
print(df.isnull().any())
#sns.heatmap(df.isnull(), yticklabels= False, annot=True, cmap="coolwarm")
#plt.title("Missing Values Heatmap")
#plt.show()
df_dropall = df.dropna(how="all")
data_Cleaned = df_dropall.interpolate()
print(data_Cleaned)
data_Cleaned.to_csv("Cleaned_Data.csv", index = False)
