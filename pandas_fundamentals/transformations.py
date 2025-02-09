import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# renaming columns
df = df.rename(columns={"old_name": "new_name"})

# casting columns
df["col"] = df["col"].astype("float")

df["col"] = pd.to_datetime(df["col"])

df["sepal_length_doubled"] = df["sepal_length"] * 2
