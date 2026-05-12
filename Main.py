import pandas  as pd
import numpy as np
import matplotlib.pyplot as p
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

data = pd.read_csv("petrol_consumption.csv")
print(data.info())
print(data.head())
print(data.isnull().any())


x = data[["Petrol_tax", "Average_income", "Paved_Highways", "Population_Driver_licence(%)"]]
y = data["Petrol_Consumption"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(x_train, y_train)
coeficcient_data = pd.DataFrame(regressor.coef_, x.columns, columns = ["Coefficient"])
print(coeficcient_data)
y_prediction = regressor.predict(x_test)
dataset = pd.DataFrame({"Actual":y_test, "Predicted":y_prediction})
print(dataset)
print(f"mean absolute error is {metrics.mean_absolute_error(y_test, y_prediction)}")
print(f"Mean squared error is {metrics.mean_squared_error(y_test, y_prediction)}")
print(f"root mean squared error {np.sqrt(metrics.mean_squared_error(y_test, y_prediction))}")

