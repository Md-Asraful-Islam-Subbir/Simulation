from numpy import random
import numpy as np
import sympy as sy

a = 2
b = 5
N = 10000

def func(x):
    return x**3

x = sy.Symbol("x")
e = sy.integrate(func(x), (x, a, b))
exact_value = float(e)  # Convert to float for easier comparison
print("Exact integral value =", exact_value)

# Generate N random samples within [a, b]
xrand = random.uniform(a, b, N)

# Monte Carlo Integration
integral = np.mean([func(xi) for xi in xrand])  # Average of function values at random points
monte_carlo_value = (b - a) * integral  # Scale by the interval length

print("Simulated integral value =", monte_carlo_value)
print("Actual integral value =", exact_value)
