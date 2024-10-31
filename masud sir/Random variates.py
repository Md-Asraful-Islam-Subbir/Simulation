import numpy as np
import matplotlib.pyplot as plt


# Function to generate random variates using inverse transform method
def inverse_transform_exponential(lambda_rate, num_variates):
    # Step 1: Generate uniform random numbers U between 0 and 1
    U = np.random.uniform(0, 1, num_variates)

    # Step 2: Apply the inverse CDF of the exponential distribution
    random_variates = -np.log(1 - U) / lambda_rate

    return random_variates


# Input: lambda (rate parameter) and number of variates
lambda_rate = float(input("Enter the rate parameter (λ) for the exponential distribution: "))
num_variates = int(input("Enter the number of random variates to generate: "))

# Generate random variates
random_variates = inverse_transform_exponential(lambda_rate, num_variates)

# Output: Display the generated random variates
print("Generated Random Variates: ")
print(random_variates)

# Plot a histogram of the generated variates
plt.hist(random_variates, bins=30, density=True, alpha=0.7, color='g')

# Overlay the theoretical PDF of the exponential distribution
x = np.linspace(0, np.max(random_variates), 100)
pdf = lambda_rate * np.exp(-lambda_rate * x)
plt.plot(x, pdf, 'r-', lw=2)

plt.title(f"Histogram of {num_variates} Exponential Random Variates")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
