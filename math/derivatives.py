import sympy as sp

# Define a symbolic variable x, a function f, and compute its derivative with respect to x
x = sp.Symbol("x")
f = x ** 2
derivative = sp.diff(f, x)

# Define a second-degree function g = 3*x**2 + 2*x + 1 and compute its derivative
g = 3 * x ** 2 + 2 * x + 1
derivative_g = sp.diff(g, x)

# Define symbolic variables x, y, a function f, and compute the partial derivatives (gradient components) with respect to x and y
x, y = sp.symbols("x y")
f = x ** 2 + y ** 2
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)

import numpy as np

# Define gradient descent function
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        error = predictions - y
        gradients = (1/m) * np.dot(X.T, error)
        theta -= learning_rate * gradients
    return theta


# Sample data for testing gradient descent
X = np.array([[1, 1], [1, 2], [1, 3]])  # Feature matrix with bias term
y = np.array([1, 2, 3])  # Target values
theta = np.array([0.1, 0.1])  # Initial values for parameters
learning_rate = 0.1  # Learning rate
iterations = 1000  # Number of iterations

# Call gradient descent function with sample data
final_theta = gradient_descent(X, y, theta, learning_rate, iterations)
print("Theta after gradient descent:", final_theta)
