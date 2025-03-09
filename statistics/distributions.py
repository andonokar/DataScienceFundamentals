import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, uniform, skew, kurtosis
from sympy.abc import alpha
import seaborn as sns

# Gaussian Distribution
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, loc=0, scale=1), label="Gaussian (u=0, s=1)")

# Binomial Distribution
n, p = 10, 0.5
x = np.arange(0, n+1)
plt.bar(x, binom.pmf(x, n, p), alpha=0.7, label="Binomial (n=10,  p=0.5)")

# Poisson Distribution
lam = 3
x = np.arange(0, 10)
plt.bar(x, poisson.pmf(x, lam), alpha=0.7, label="Poisson")

# Uniform Distribution
x = np.random.uniform(low=0, high=10, size=1000)
sns.histplot(x, kde=True, label="Uniform", color="red")

plt.title("distributions")
plt.legend()
plt.show()

# Load dataset
df = sns.load_dataset("iris")

# Analyse sepal_length
feature = df["sepal_length"]
print(skew(feature))
print(kurtosis(feature))

# Visualize
sns.histplot(feature, kde=True)
plt.title("distribution")
plt.show()