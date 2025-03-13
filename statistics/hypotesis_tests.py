from scipy.stats import chi2_contingency, f_oneway, ttest_ind, ttest_1samp, ttest_rel

# Contigency Table
data = [[50, 30], [20, 40]]

# Perform Chi-Square Test
chi2, p, dof, expected = chi2_contingency(data)
print(f"{chi2=}")
print(f"{p=}")
print(f"{dof=}")
print(f"{expected=}")

# DAta for three groups
group1 = [12, 14, 15, 16, 17]
group2 = [11, 13, 14, 15, 16]
group3 = [10, 12, 13, 14, 15]

# Perform ANOVA
f_stat, p_value = f_oneway(group1, group2, group3)
print(f"{f_stat=}")
print(f"{p_value=}")

# Conduct T-tests
# Perform one-sample, two-sample, paired t-tests

# One-Sample T-Test
data = [12, 14, 15, 16, 17]
mean = 15
t_stat, p_value = ttest_1samp(data, mean)
print(f"{t_stat=}, {p_value=}")

# Two-Sample T-Test
group1 = [12, 14, 15, 16, 17]
group2 = [11, 13, 14, 15, 16]
t_stat, p_value = ttest_ind(group1, group2)
print(f"{t_stat=}, {p_value=}")

# Paired T-Test
pre_test = [12, 14, 15, 16, 17]
post_test = [13, 14, 16, 17, 18]
t_stat, p_value = ttest_rel(pre_test, post_test)
print(f"{t_stat=}, {p_value=}")
