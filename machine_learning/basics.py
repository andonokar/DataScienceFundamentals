import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")

# Define features and targets
features = df[["total_bill", "size"]]
target = df["tip"]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Visualize relationships
sns.pairplot(df, x_vars=["total_bill", "size"], y_vars="tip", height=5, aspect=0.8, kind="scatter")
plt.title("feature vs target")
plt.show()