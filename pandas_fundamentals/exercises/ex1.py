import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

print("first 5 rows \n", df.head())

print(df.info())
print(df.describe())


selected_columns = df[["species", "sepal_length"]]

filtered_rows = df[(df["sepal_length"] > 5) & (df["species"] == "setosa")]