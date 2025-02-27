from itertools import product
import random  # Import random module for simulation

from sympy.abc import alpha

# Sample space of a die roll
sample_space = list(range(1, 7))

# Probability of rolling an even number
even_numbers = [2, 4, 6]
P_even = len(even_numbers) / len(sample_space)

import numpy as np

# Random variable: die roll
outcomes = np.array(sample_space)
probabilities = np.array([1 / 6] * 6)

# Expectation
expectation = np.sum(outcomes * probabilities)
print(expectation)

# Variance and std
variance = np.sum((outcomes - expectation) ** 2 * probabilities)
std_dev = np.sqrt(variance)
print(variance, std_dev)

# Simulate rolling a die 10,000 times
rolled_numbers = np.random.randint(1, 7, 10000)

# Calculate probability of rolling an even number
P_even_simulation = np.sum(rolled_numbers % 2 == 0) / len(rolled_numbers)

# Calculate probability of rolling a number greater than four
P_greater_than_four = np.sum(rolled_numbers > 4) / len(rolled_numbers)

# Print results
print(f"Simulated Probability of Even Numbers: {P_even_simulation}")
print(f"Simulated Probability of Numbers Greater Than Four: {P_greater_than_four}")

import matplotlib.pyplot as plt
from scipy.stats import uniform

# Discrete random variable
outcomes = [1,2,3,4,5,6]
probabilities = [1/6] * 6
plt.bar(outcomes, probabilities, color="blue", alpha=0.7)
plt.title("PMF of a dice roll")
plt.xlabel("outcomes")
plt.ylabel("probability")
plt.show()

# Continuous random variable
x = np.linspace(0,1,100)
pdf = uniform.pdf(x,loc=0,scale=1)
plt.plot(x, pdf, color="red")
plt.title("pdf")
plt.xlabel("x")
plt.ylabel("fx")
plt.show()