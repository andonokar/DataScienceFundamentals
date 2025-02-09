import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

combined = pd.concat([df, df], axis=0)
combined2 = pd.concat([df, df], axis=1)

merged = pd.merge(df, df, on="col")

joined = df.join(df, how="inner")