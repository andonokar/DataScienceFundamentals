import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Generate values
z = np.linspace(-10, 10 ,100)
sigmoid_values = sigmoid(z)

# Plot
plt.plot(z, sigmoid_values)
plt.title("sigmoid function")
plt.xlabel("z")
plt.ylabel("sigma(z)")
plt.grid()
plt.show()

# Generate synthetic dataset
np.random.seed(42)
n_samples = 200
X = np.random.rand(n_samples, 2) * 10
y = (X[:, 0] * 1.5 + X[:, 1] > 15).astype(int)

# Create a Dataframe
df = pd.DataFrame(X, columns=["Age", "Salary"])
df["Purchase"] = y

# Split Data
X_train, X_test, y_train, y_test = train_test_split(df[["Age", "Salary"]], df["Purchase"], test_size=0.2,
                                                    random_state=42)

# Train Logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate performance
print(accuracy_score(y_test, y_pred))
print(precision_score(y_test, y_pred))
print(recall_score(y_test, y_pred))
print(f1_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

# Predict probabilities for grid points
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, Z, alpha=0.8, cmap="coolwarm")
plt.scatter(X_test["Age"], X_test["Salary"], c=y_test, edgecolor="k", cmap="coolwarm")
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("age")
plt.ylabel("salary")
plt.show()