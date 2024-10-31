import numpy as np
from scipy.stats import chi2

# Parameters for random number generation
num_random_numbers = 100  # Total number of random numbers to generate
min_value = 1             # Minimum value (inclusive)
max_value = 100           # Maximum value (inclusive)

# Generate random numbers
random_numbers = np.random.randint(min_value, max_value + 1, num_random_numbers)

# Create pairs from the random numbers
pairs = []
for i in range(0, len(random_numbers) - 1):
    pairs.append((random_numbers[i], random_numbers[i + 1]))

print("Generated Random Numbers:", random_numbers)
print("Pairs:", pairs)
print("Total number of pairs:", len(pairs))

# Initialize counts for each class
class_counts = np.zeros(9)

# Classify the pairs
for pair in pairs:
    if pair[0] <= 33 and pair[1] <= 33:
        class_counts[0] += 1
    elif pair[0] <= 67 and pair[1] <= 33:
        class_counts[1] += 1
    elif pair[0] <= 100 and pair[1] <= 33:
        class_counts[2] += 1
    elif pair[0] <= 33 and pair[1] <= 67:
        class_counts[3] += 1
    elif pair[0] <= 67 and pair[1] <= 67:
        class_counts[4] += 1
    elif pair[0] <= 100 and pair[1] <= 67:
        class_counts[5] += 1
    elif pair[0] <= 33 and pair[1] <= 100:
        class_counts[6] += 1
    elif pair[0] <= 67 and pair[1] <= 100:
        class_counts[7] += 1
    elif pair[0] <= 100 and pair[1] <= 100:
        class_counts[8] += 1

# Calculate the expectation of pairs in each class
expected_counts = np.full(9, len(pairs) / 9)

# Calculate the chi-squared statistic
chi2_stat = np.sum((class_counts - expected_counts) ** 2 / expected_counts)

# Calculate the degrees of freedom
df = len(class_counts) - 1

# Calculate the critical value for alpha = 0.05
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, df)

# Print the test results
print("Class Counts:", class_counts)
print("Expected Counts:", expected_counts)
print("Chi-squared statistic:", chi2_stat)
print("Critical value for alpha 0.05:", critical_value)

# Check if the null hypothesis is rejected
if chi2_stat > critical_value:
    print("Reject the null hypothesis: The distribution is not uniform.")
else:
    print("Fail to reject the null hypothesis: The distribution is uniform.")
