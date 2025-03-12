import numpy as np
from scipy.stats import ttest_1samp, ttest_ind

# Sample data
data = [12, 14, 15, 16, 17, 18, 19]

# Null hypothesis: mean
population_mean = 15

# Perform t-test
t_stat, p_value = ttest_1samp(data, population_mean)
print("T-statistic: ", t_stat)
print("P-Value", p_value)

# Interpret results
alpha = 0.05
if p_value <= alpha:
    print("reject")
else:
    print("fail to reject")

# Data from two groups
group1 = [12, 14, 15, 16, 18, 19]
group2 = [11, 13, 14, 15, 16, 17, 18]

# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print(f"{t_stat=}")
print(f"{p_value=}")

# Interpretation
alpha = 0.05
if p_value <= alpha:
    print("reject")
else:
    print("failed to reject")