import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# drop missing values
df = df.dropna()

# drop columns with missing values
df = df.dropna(axis=1)

df["column_name"] = df["column_name"].fillna(0)

df.fillna(method="ffill")
df.fillna(method="bfill")

df["column_name"] = df["column_name"].interpolate()
