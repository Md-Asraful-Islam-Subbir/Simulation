import numpy as np
import matplotlib.pyplot as plt

# Function to generate Bernoulli distribution
def bernoulli_distribution(p, n):
    """
    Generates Bernoulli distribution samples.

    Parameters:
    p (float): Probability of success (0 <= p <= 1)
    n (int): Number of trials

    Returns:
    np.array: Array of 1's and 0's representing success and failure.
    """
    return np.random.binomial(1, p, n)

# Parameters
p = 0.5  # Probability of success
n = 1000  # Number of trials

# Generate Bernoulli distribution
samples = bernoulli_distribution(p, n)

# Calculate frequency of outcomes
unique, counts = np.unique(samples, return_counts=True)
outcome_counts = dict(zip(unique, counts))

# Display outcomes
print(f"Outcome counts: {outcome_counts}")

# Plotting the Bernoulli distribution
plt.bar(outcome_counts.keys(), outcome_counts.values(), tick_label=["Failure (0)", "Success (1)"])
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title(f'Bernoulli Distribution (p = {p})')
plt.show()
