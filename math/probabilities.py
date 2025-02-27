def bayes_theorem(p_b_given_a, p_a, p_b):
    """
    Calculate the posterior probability using Bayes' Theorem.
    
    Parameters:
    p_b_given_a (float): Probability of B given A (P(B|A)).
    p_a (float): Probability of A (P(A)).
    p_b (float): Probability of B (P(B)).
    
    Returns:
    float: Posterior probability P(A|B).
    """
    if p_b == 0:
        raise ValueError("Probability of B (p_b) cannot be zero.")
    return (p_b_given_a * p_a) / p_b


def binomial_distribution(n=10, p=0.5, sample_size=1000, visualize=False):
    """
    Generate a Binomial distribution with the given parameters and optionally visualize it.

    Parameters:
    n (int): Number of trials.
    p (float): Probability of success in each trial. Must be between 0 and 1.
    sample_size (int): Number of samples to generate.
    visualize (bool): If True, visualize the distribution using a histogram.

    Returns:
    numpy.ndarray: Array containing samples from the Binomial distribution.
    """
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")

    if n <= 0:
        raise ValueError("Number of trials n must be greater than zero.")

    data = np.random.binomial(n, p, sample_size)

    if visualize:
        plt.hist(data, bins=n + 1, density=True, alpha=0.7, color='green', range=(0, n + 1))
        plt.title(f"Binomial Distribution (n={n}, p={p})")
        plt.xlabel("Number of Successes")
        plt.ylabel("Frequency")
        plt.show()

    return data


import numpy as np
import matplotlib.pyplot as plt


def poisson_distribution(mean=1, sample_size=1000, visualize=False):
    """
    Generate a Poisson distribution with the given mean and optionally visualize it.

    Parameters:
    mean (float): Mean (lambda) of the Poisson distribution. Must be greater than 0.
    sample_size (int): Number of samples to generate.
    visualize (bool): If True, visualize the distribution using a histogram.

    Returns:
    numpy.ndarray: Array containing samples from the Poisson distribution.
    """
    if mean <= 0:
        raise ValueError("Mean (lambda) must be greater than 0.")

    data = np.random.poisson(mean, sample_size)

    if visualize:
        plt.hist(data, bins=range(min(data), max(data) + 2), density=True, alpha=0.7, color='purple', edgecolor='black',
                 align='left')
        plt.title(f"Poisson Distribution (mean={mean})")
        plt.xlabel("Occurrences")
        plt.ylabel("Frequency")
        plt.show()

    return data


def bernoulli_distribution(p=0.5, sample_size=1000, visualize=False):
    """
    Generate a Bernoulli distribution with a given probability of success and optionally visualize it.
    
    Parameters:
    p (float): Probability of success (1). Must be between 0 and 1.
    sample_size (int): Number of samples to generate.
    visualize (bool): If True, visualize the distribution with a bar chart.
    
    Returns:
    numpy.ndarray: Array containing samples from the Bernoulli distribution (0s and 1s).
    """
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")

    data = np.random.binomial(1, p, sample_size)

    if visualize:
        unique, counts = np.unique(data, return_counts=True)
        plt.bar(unique, counts, color='orange', tick_label=['0', '1'])
        plt.title(f"Bernoulli Distribution (p={p})")
        plt.xlabel("Outcome")
        plt.ylabel("Frequency")
        plt.show()

    return data


def normal_distribution(mean=0, std_dev=1, sample_size=1000, visualize=False):
    """
    Generate a normal distribution with given parameters and optionally visualize it.
    
    Parameters:
    mean (float): Mean of the normal distribution.
    std_dev (float): Standard deviation of the normal distribution.
    sample_size (int): Number of samples to generate.
    visualize (bool): If True, visualize the distribution using a histogram.
    
    Returns:
    numpy.ndarray: Array containing samples from the normal distribution.
    """
    data = np.random.normal(mean, std_dev, sample_size)
    if visualize:
        plt.hist(data, bins=30, density=True, alpha=0.7, color='blue')
        plt.title(f"Normal Distribution (mean={mean}, std_dev={std_dev})")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
    return data




