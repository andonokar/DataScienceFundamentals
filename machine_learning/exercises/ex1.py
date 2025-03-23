import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Load the California Housing dataset
data = fetch_california_housing(as_frame=True)
df = data.frame

# Select feature (Median Income) and target(Median House Value)
X = df[["MedInc"]]
y = df[["MedHouseVal"]]

# Transform feature to polynomial features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Fit polynomial regression model
model = LinearRegression()
model.fit(X_poly, y)

# Make Predictions
y_pred = model.predict(X_poly)

# Plot actual vs predicted value
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="Blue", label="Actual Data", alpha=0.5)
plt.scatter(X, y_pred, color="Blue", label="predicted Data", alpha=0.5)
plt.title("Polynomial Regression")
plt.xlabel("Media income in california")
plt.ylabel("median house value in california")
plt.legend()
plt.plot()

# Evaluate model performance
mse = mean_squared_error(y, y_pred)
print(f"{mse=}")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Ridge Regression
ridge_model = Ridge(alpha=1)
ridge_model.fit(X_train, y_train)
ridge_predictions = ridge_model.predict(X_test)

# Lasso Regression
lasso_model = Lasso(alpha=1)
lasso_model.fit(X_train, y_train)
lasso_predictions = lasso_model.predict(X_test)

# Evaluate Ridge
ridge_mse = mean_squared_error(y_test, ridge_predictions)
print(f"{ridge_mse=}")

# Evaluate Lasso
lasso_mse = mean_squared_error(y_test, lasso_predictions)
print(f"{lasso_mse=}")

# Visualize Ridge vs Lasso predictions
plt.figure(figsize=(10,6))
plt.scatter(X_test[:, 0], y_test, color="blue", label="Actual Data", alpha=0.5)
plt.scatter(X_test[:, 0], ridge_predictions, color="green", label="Ridge Predictions", alpha=0.5)
plt.scatter(X_test[:, 0], lasso_predictions, color="orange", label="Ridge Predictions", alpha=0.5)
plt.title("ridge vs lasso")
plt.xlabel("Median income transformed")
plt.ylabel("Median house value in california")
plt.legend()
plt.show()