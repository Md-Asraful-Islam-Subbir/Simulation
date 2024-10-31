import random
import math

# Initialize variables
vf = float(input("Enter the speed of the fighter plane (km/min): "))  # Fighter plane speed
time = 0  # Initial time

# Get initial positions from the user
xf = int(input("Enter the initial x-coordinate of the fighter plane: "))
yf = int(input("Enter the initial y-coordinate of the fighter plane: "))
xb = int(input("Enter the initial x-coordinate of the bomber plane: "))
yb = int(input("Enter the initial y-coordinate of the bomber plane: "))

flag = 0

while flag == 0:
    # Calculate the distance between the fighter and bomber planes
    distance = math.sqrt((xf - xb) ** 2 + (yf - yb) ** 2)

    if distance <= 100:
        print("The Bomber Plane Shot Down at time", time)
        print(f"\nPursuit ends, shot at {time} minutes and at {distance:.2f} km.")
        flag = 1
    elif distance > 1000:
        print("The Bomber Plane Escapes at time", time)
        print(f"\nPursuit ends, escape at {time} minutes and at {distance:.2f} km.")
        flag = 1
    else:
        # Update the fighter plane's position to move towards the bomber
        xf += vf * (xb - xf) / distance
        yf += vf * (yb - yf) / distance

        # Randomly update bomber's position
        xb = random.randint(1, 1000)
        yb = random.randint(1, 1000)
        time += 1
