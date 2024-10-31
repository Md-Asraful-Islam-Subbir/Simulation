import numpy as np
import matplotlib.pyplot as plt
import math


# Function to calculate Poisson PMF
def poisson_pmf(lambd, k):
    return (lambd ** k) * np.exp(-lambd) / math.factorial(k)

def plot_poisson_pmf(lambd, max_calls):
    # Calculate probabilities for 0 to max_calls
    k_values = np.arange(0, max_calls + 1)
    probabilities = [poisson_pmf(lambd, k) for k in k_values]

    # Plot the PMF
    plt.bar(k_values, probabilities, alpha=0.75, color='b', label=f'λ = {lambd}')
    plt.title(f'Poisson Distribution (λ = {lambd})')
    plt.xlabel('Number of Calls')
    plt.ylabel('Probability')
    plt.xticks(k_values)
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print the probabilities for each number of calls
    for k, prob in zip(k_values, probabilities):
        print(f"P(X = {k}) = {prob:.4f}")


# Simulate and plot Poisson PMF for λ = 5, considering calls from 0 to 10
print("Poisson Distribution for λ = 5 (0 to 10 calls):")
plot_poisson_pmf(5, 10)

# Simulate and plot Poisson PMF for λ = 10, considering calls from 0 to 15
print("Poisson Distribution for λ = 10 (0 to 15 calls):")
plot_poisson_pmf(10, 15)

# Simulate and plot Poisson PMF for λ = 15, considering calls from 0 to 15
print("Poisson Distribution for λ = 15 (0 to 15 calls):")
plot_poisson_pmf(15, 15)
