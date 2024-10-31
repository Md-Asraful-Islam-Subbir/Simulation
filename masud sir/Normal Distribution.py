import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set parameters for the normal distributions
sample_size = 200
mean1, std_dev1 = 100, 20  # First distribution parameters
mean2, std_dev2 = 80, 20   # Second distribution parameters (diastolic blood pressure for men)

# Generate samples
data1 = np.random.normal(mean1, std_dev1, sample_size)  # For unimodal
data2 = np.random.normal(mean2, std_dev2, sample_size)  # For second mode in multimodal

# Plot Unimodal Distribution
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.histplot(data1, bins=20, kde=True, color='skyblue', stat="density")
plt.title("Unimodal Distribution (Mean=100, Std Dev=20)")
plt.xlabel("Value")
plt.ylabel("Density")

# Plot Multimodal Distribution by combining data1 and data2
combined_data = np.concatenate([data1, data2])

plt.subplot(1, 2, 2)
sns.histplot(combined_data, bins=30, kde=True, color='salmon', stat="density")
plt.title("Multimodal Distribution (Mean=100 and Mean=80, Std Dev=20)")
plt.xlabel("Value")
plt.ylabel("Density")

plt.tight_layout()
plt.show()
