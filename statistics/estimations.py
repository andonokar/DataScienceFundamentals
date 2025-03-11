import numpy as np
from scipy.stats import norm, t
import seaborn as sns

# Sample Data
data = [12, 14, 15, 16, 17, 18, 19]
mean = np.mean(data)
std = np.std(data, ddof=1)

# 95% Confidence Interval(t-distribution)
n = len(data)
t_value = t.ppf(0.975, df=n-1)
margin_error = t_value * (std / np.sqrt(n))
ci =  (mean - margin_error, mean + margin_error)
print(ci)

# Generate random sample data
data  = np.random.normal(loc=50, scale=10, size=100)

# Sample statistics
mean = np.mean(data)
std = np.std(data, ddof=1)
n = len(data)

# 95% Confidence Interval
z_value = norm.ppf(0.975)
margin_error = z_value * (std / np.sqrt(n))
ci = (mean - margin_error, mean + margin_error)

print(mean)
print(ci)

# Load iris datset
df = sns.load_dataset("iris")

# Sampling
sample = df["sepal_length"].sample(30, random_state=42)

# Sample statistics
mean = sample.mean()
std = sample.std()
n = len(sample)

# Confidence Interval
z_value = norm.ppf(0.975)
margin_error = z_value * (std / np.sqrt(n))
ci = (mean - margin_error, mean + margin_error)
print(mean)
print(ci)