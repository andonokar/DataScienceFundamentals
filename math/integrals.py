import sympy as sp

x = sp.Symbol("x")
integral = sp.integrate(x ** 2, x)
print(f"The integral of x^2 with respect to x is: {integral}")
print(f"The value of sp.oo is: {sp.oo}")

definite_integral = sp.integrate(x ** 2, (x, 0, 2))
print(f"The definite integral of x^2 from 0 to 2 is: {definite_integral}")

# Synthetic dataset
import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3]])  # Feature matrix with bias term
y = np.array([3, 5, 7])  # Target values


# Synthetic gradient calculation
def compute_gradient(X, y, weights):
    predictions = np.dot(X, weights)
    errors = predictions - y
    gradient = (1 / len(y)) * np.dot(X.T, errors)
    return gradient


# Stochastic Gradient Descent (SGD) implementation
def sgd(X, y, weights, learning_rate, epochs):
    for epoch in range(epochs):
        for i in range(len(y)):
            gradient = compute_gradient(X[i:i + 1], y[i:i + 1], weights)
            weights -= learning_rate * gradient
    return weights


# Initialize weights and perform SGD
weights = np.zeros(X.shape[1])
learning_rate = 0.01
epochs = 100

trained_weights = sgd(X, y, weights, learning_rate, epochs)
print(f"Trained weights after SGD: {trained_weights}")
