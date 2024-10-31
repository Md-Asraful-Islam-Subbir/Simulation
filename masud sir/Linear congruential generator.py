def linear_congruential_generator(seed, a, c, m, num_random_numbers):
    # List to store generated random numbers
    random_numbers = []

    # Initialize the first value with the seed
    x = seed

    # Generate random numbers
    for _ in range(num_random_numbers):
        # Apply the LCG formula
        x = (a * x + c) % m
        # Normalize the result to get a uniform random number between 0 and 1
        random_numbers.append(x / m)

    return random_numbers


# Input parameters for the LCG
seed = int(input("Enter the seed (initial value): "))
a = int(input("Enter the multiplier (a): "))
c = int(input("Enter the increment (c): "))
m = int(input("Enter the modulus (m): "))
num_random_numbers = int(input("Enter the number of random numbers to generate: "))

# Generate random numbers using LCG
random_numbers = linear_congruential_generator(seed, a, c, m, num_random_numbers)

# Output the generated random numbers
print("Generated Random Numbers (Uniform[0,1]):")
for i, rand_num in enumerate(random_numbers, 1):
    print(f"{i}: {rand_num:.6f}")
