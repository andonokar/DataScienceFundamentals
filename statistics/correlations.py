import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression

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

print("Slope", model.coef_[0])
print("Intercept", model.intercept_)
print("R-squared", model.score(x, y))