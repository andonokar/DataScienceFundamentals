import pandas as pd
import numpy as np

data = {
    "name": ["Lia", "Bob", "Charlie", np.nan, "lia"],
    "age": [29, np.nan, 30, 22, np.nan],
    "score": [85, np.nan, 92, 77, np.nan]
}

df = pd.DataFrame(data)

df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].interpolate()

df = df.rename(columns={"name": "student_name", "score": "exam_score"})

df["student_id"] = [1, 2, 3, 4, 5]

data2 = {
    "student_id": [1, 2, 3, 4, 5],
    "major": ["Math", "Science", "Literature", "Engineering", "Art"]
}
df2 = pd.DataFrame(data2)

merged_df = pd.merge(df, df2, on="student_id")

merged_df = merged_df.dropna(axis=1, thresh=len(merged_df) // 2)

merged_df = pd.concat([merged_df, pd.get_dummies(merged_df["major"], prefix="major")], axis=1)

print(merged_df)