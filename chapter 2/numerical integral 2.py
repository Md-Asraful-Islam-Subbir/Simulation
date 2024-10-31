import random
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate  # Import tabulate library for table formatting


def func(x):
    return x ** 3


# Get user input for the number of random points
n = int(input("Enter the number of random points (n): "))  # Total number of points
m = 0  # Points under the curve
data = []  # To store the points and their respective results

# Generate random points based on user input
for i in range(n):
    # Manual input for x and y
    rx = float(input(f"Enter x value for point {i + 1} (between 2.0 and 5.0): "))
    ry = float(input(f"Enter y value for point {i + 1} (between 0 and 140): "))

    # Validate the inputs
    if not (2.0 <= rx <= 5.0):
        print("Invalid x value. It must be between 2.0 and 5.0.")
        continue
    if not (0 <= ry <= 140):
        print("Invalid y value. It must be between 0 and 140.")
        continue

    function_value = func(rx)  # Calculate the function value for current rx

    # Append data for table
    data.append([m, n, rx, ry, function_value])

    if ry <= function_value:
        m += 1
        plt.scatter(rx, ry, color="green")  # Points under the curve
    else:
        plt.scatter(rx, ry, color="blue")  # Points above the curve

# Prepare data for plotting the function
x_vals = np.arange(0, 10, 0.2)
y_vals = func(x_vals)

# Plot the function
plt.plot(x_vals, y_vals, color="red", label="y = x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Integration Visualization")
plt.legend()
plt.show()

# Calculate the area under the curve using the Monte Carlo method
rectangle_area = (5.0 - 2.0) * 140  # Width of rectangle * Height
estimated_area = (m / n) * rectangle_area

# Print the data in a table
table_headers = ["M (Points under Curve)", "N (Total Points)", "Random X", "Random Y", "Function Value (y = x^3)"]
print(tabulate(data, headers=table_headers, tablefmt="grid"))

# Print estimated area under the curve
print(f"\nEstimated Area Under the Curve: {estimated_area:.2f}")
