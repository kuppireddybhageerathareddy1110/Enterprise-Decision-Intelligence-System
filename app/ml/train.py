import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("app/data/sample_data.csv")

X = df[["revenue", "cost", "employees"]]
y = df["customer_satisfaction"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "models/decision_model.pkl")
print("Model trained and saved")
