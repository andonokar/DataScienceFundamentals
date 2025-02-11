import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")

# Inspect Data
print(df.info())
print(df.describe())

# Handle missing data
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# filter passengers in first class
first_class = df[df["Pclass"] == 1]
print(first_class)

# Bar chart: survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="skyblue")
plt.title("survival by class")
plt.ylabel("rate")
plt.show()

# Histogram: Age distribution
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age distribution")
plt.xlabel("age")
plt.ylabel("frequency")
plt.show()

# age vs fare
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color="green")
plt.title("age vs fare")
plt.xlabel("age")
plt.ylabel("fare")
plt.show()