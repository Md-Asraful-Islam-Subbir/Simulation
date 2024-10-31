import numpy as np
import matplotlib.pyplot as plt

# Get user input for dimensions of the target area
x = int(input("Enter the width (x) of the target area: "))
y = int(input("Enter the height (y) of the target area: "))

# Standard deviations based on the dimensions of the area
standard_deviation_x = x
standard_deviation_y = y

# Get user input for number of simulations and strikes per simulation
number_of_simulation = int(input("Enter the number of simulations: "))
number_of_strike_each_simulation = int(input("Enter the number of strikes per simulation: "))

# Run simulations
for sim in range(number_of_simulation):
    hit = 0
    miss = 0
    point_x = []
    point_y = []

    for i in range(number_of_strike_each_simulation):
        # Generate random points with a normal distribution
        current_x = standard_deviation_x * np.random.randn()
        current_y = standard_deviation_y * np.random.randn()

        point_x.append(current_x)
        point_y.append(current_y)

        # Check if the point is within the target area
        if abs(current_x) <= standard_deviation_x and abs(current_y) <= standard_deviation_y:
            hit += 1
        else:
            miss += 1

    # Print the results for each simulation
    print(f"Simulation {sim + 1}:")
    print("Number of hits =", hit)
    print("Number of misses =", miss)
    print("Strike accuracy =", round((hit / number_of_strike_each_simulation) * 100, 2), "%")

    # Plot the target area and strikes
    area_x = [-x, x, x, -x, -x]
    area_y = [-y, -y, y, y, -y]

    plt.plot(area_x, area_y, color="blue")  # Target area outline
    plt.scatter(point_x, point_y, color="red")  # Points for strikes
    plt.axis('equal')
    plt.title(f"Simulation {sim + 1}")
    plt.show()
