import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

# Pearson Correlation
r, _ = pearsonr(x, y)
print(f"{r=}")

# Spearman Correlation
rho, _ = spearmanr(x, y)
print(f"{rho=}")

# Sample Data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 8, 10])

# Fit Linear Regression
model = LinearRegression()
model.fit(x, y)

print("Slope", slope := model.coef_[0])
print("Intercept", intercept := model.intercept_)
print("R-squared", score := model.score(x, y))

plt.scatter(x, y, color="blue", label="Data")
plt.plot(x, model.predict(x), color="red", label="LR")
plt.legend()
plt.show()

# Load dataset
df = sns.load_dataset("iris")
del df["species"]

# Compute correlation matrix
corr = df.corr()

# Plot heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("feature correlations")
plt.show()