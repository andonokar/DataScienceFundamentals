import pandas as pd

data = {
    "Class": ["A", "B", "A", "C", "C", "D", "B", "A", "A", "B"],
    "Score": [85, 90, 78, 92, 88, 76, 95, 89, 84, 91],
    "Age": [15, 16, 15, 17, 16, 14, 18, 17, 15, 16]
}

df = pd.DataFrame(data)
print(df)
grouped_df = df.groupby("Class").mean()
print(grouped_df)
variance = df.groupby("Class").var()
print(variance)
stats = df.groupby("Class").apply(lambda x: x.describe())
print(stats)