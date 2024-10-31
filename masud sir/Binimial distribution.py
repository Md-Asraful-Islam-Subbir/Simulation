import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Function to generate samples from a Binomial distribution
def binomial_distribution(n, p, trials):
    """
    Generates samples from a Binomial distribution.

    Parameters:
    n (int): Number of trials in each experiment.
    p (float): Probability of success in each trial.
    trials (int): Number of experiments to conduct.

    Returns:
    np.array: Array of success counts from each experiment.
    """
    return np.random.binomial(n, p, trials)

# Parameters
n = 10        # Number of trials per experiment
p = 0.5       # Probability of success in each trial
trials = 1000 # Number of experiments

# Generate Binomial distribution samples
samples = binomial_distribution(n, p, trials)

# Calculate the frequency of each outcome
unique, counts = np.unique(samples, return_counts=True)
outcome_counts = dict(zip(unique, counts))

# Display the frequency of outcomes
print(f"Outcome counts: {outcome_counts}")

# Plotting the Binomial distribution
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

# Plotting observed frequencies
plt.figure(figsize=(10, 6))
plt.bar(outcome_counts.keys(), outcome_counts.values(), label="Observed Frequencies", color='lightblue')
plt.plot(x, trials * pmf, marker='o', color='red', linestyle='-', label="Expected Binomial PMF")
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.title(f'Binomial Distribution (n = {n}, p = {p})')
plt.legend()
plt.show()
