import pandas as pd

# creating a series
s = pd.Series([10,20,30], index=["a", "b", "c"])

# creating dataframe
data = {"name": ["Lia", "ander"], "age": [29, 28]}
df = pd.DataFrame(data)

# creating from csv
df_csv = pd.read_csv("data.csv")
df_xlsx = pd.read_excel("data.xlsx")

# save the data
df_csv.to_csv(..., index=False)
df_csv.to_excel(..., index=False)