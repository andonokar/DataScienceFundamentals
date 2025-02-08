import pandas as pd
data = {"name": ["Lia", "ander"], "age": [29, 28]}
df = pd.DataFrame(data)

# view data
print(df.head())
print(df.tail())

# view info
print(df.info())
print(df.describe())

# selecting column
print(df["name"])
print(df.name)
print(df[["name","age"]])

# filtering rows
print(df[df["age"] > 25])

# getting data for first row
print(df.iloc[0])

# getting first column
print(df.iloc[:, 0])

# getting by label
print(df.loc[0])
print(df.loc[:, "name"])
