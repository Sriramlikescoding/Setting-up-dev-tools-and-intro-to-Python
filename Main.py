import matplotlib.pyplot as p
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1,1)
y = np.array([0,1,0,0, 1, 1, 1, 1, 1, 1]).reshape(-1,1)
model = LogisticRegression(solver='liblinear', C = 10.0, random_state=0)
model.fit(x,y)
xprediction = model.predict_proba(x)
yprediction = model.predict(x)
#x1prediction = model.predict(x)
score = model.score(x,y)
cm = confusion_matrix(y, yprediction)
report = classification_report(y, yprediction)
print(f"x:{x} y:{y}")
print(f"x:{x}\n")
print(f"y: {y}")
print(f"intercept:{model.intercept_}")
print(f"Coefficient: {model.coef_}")
print(f"xprediction = {xprediction}")
print(f"yprediction = {yprediction}")

