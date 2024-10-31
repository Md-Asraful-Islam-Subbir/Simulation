import random
import scipy.stats as stats

observed_frequencies = {
    'Five different digits': 3075,
    'Pairs': 4935,
    'Two pairs': 1135,
    'Three of a kind': 695,
    'Full houses': 105,
    'Four of a kind': 54,
    'Five of a kind': 1
}


total_numbers = sum(observed_frequencies.values())

print("Observed frequencies:")
for combination, count in observed_frequencies.items():
    print(f"{combination}: {count} ({count / total_numbers * 100:.2f}%)")

expected_frequencies = {
    'Five different digits': total_numbers * 0.3024,
    'Pairs': total_numbers * 0.5040,
    'Two pairs': total_numbers * 0.1080,
    'Three of a kind': total_numbers * 0.0720,
    'Full houses': total_numbers * 0.0090,
    'Four of a kind': total_numbers * 0.0045,
    'Five of a kind': total_numbers * 0.0001
}


print("===")
print(expected_frequencies)
print("===")


chi_square = 0
for combination in observed_frequencies:
    observed = observed_frequencies[combination]
    expected = expected_frequencies[combination]
    chi_square += (observed - expected) ** 2 / expected

print("Chi-square statistic:", chi_square)

df = len(observed_frequencies) - 1

# Significance level (alpha)
alpha = 0.05

# Critical chi-square value
critical_chi_square = stats.chi2.ppf(1 - alpha, df)

if chi_square > critical_chi_square:
    print("Reject the null hypothesis. The random numbers are not independent.")
else:
    print("Not reject the null hypothesis. The random numbers are independent.")