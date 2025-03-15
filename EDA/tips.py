import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import ttest_ind

# Load Dataset
df = sns.load_dataset("tips")

# Inspect Data
print(df.info())
print(df.describe())

# Visualize Distributions
sns.histplot(df["total_bill"], kde=True)
plt.title("total bill")
plt.show()

# Correlation heatmap
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
plt.title("correlation")
plt.show()

# Separate data by gender
male_tips = df[df["sex"] == "Male"]["tip"]
female_tips = df[df["sex"] == "Female"]["tip"]

# Perform t-test
t_stat, p_value = ttest_ind(male_tips, female_tips)
print(f"{t_stat=}")
print(f"{p_value=}")

# Interpret result
alpha = 0.5
if p_value <= alpha:
    print("Reject all null hypothesis")
else:
    print("fail to reject")

# Define variables
X = df["total_bill"].values.reshape(-1, 1)
y = df["tip"].values

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Output coefficients
print("Slope", slope := model.coef_[0])
print("Intercept", intercept := model.intercept_)
print("R-squared", score := model.score(X, y))

# Plot regression
sns.scatterplot(x=df["total_bill"], y=df["tip"], color="blue")
plt.plot(df["total_bill"], model.predict(X), color="red", label="LR")
plt.legend()
plt.show()