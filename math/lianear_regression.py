import numpy as np

# Formula
def predict(X, theta):
    return np.dot(X, theta)


# Gradient Descent
def gradient_descent(X, y, theta, learning_rate, iteration):
    m = len(y)
    for _ in range(iteration):
        gradients = (1/m) * np.dot(X.T, (np.dot(X, theta)) - y)
        theta -= learning_rate * gradients
    return theta


# Evaluation
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)


def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_pred))**2)
    return 1 - (ss_res / ss_tot)