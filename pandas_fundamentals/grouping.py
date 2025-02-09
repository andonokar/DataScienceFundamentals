import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# group the data in pandas
grouped_df = df.groupby("species")

# display grouped data
for name, group in grouped_df:
    print(name)
    print(group)

# aggregations
print(grouped_df.mean())
print(grouped_df.sum())

# aggregating a single column
print(df.groupby("species")["sepal_length"].mean())

# Multiple aggregation functions
print(grouped_df.agg({"sepal_length": ["mean", "sum"], "petal_width": ["min", "max"]}))

# Applying custom aggregation with lambda
print(grouped_df.agg({"sepal_length": lambda x: x.max() - x.min()}))

# Descriptive statistics using apply
print(grouped_df["sepal_length"].apply(lambda x: x.describe()))

# Demonstrating the use of pivot_table with a lambda aggregation
pivot = pd.pivot_table(df, values="sepal_length", index="species", columns="petal_width",
                       aggfunc=lambda x: x.max() - x.min())
print(pivot)

