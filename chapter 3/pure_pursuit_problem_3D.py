import random
import math

# Initialize variables
flag = 0
vf = 20  # Fighter plane speed
time = 0  # Initial time

# Initial 3D positions of the fighter and bomber planes
xf, yf, zf = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
xb, yb, zb = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)

while flag == 0:
    # Calculate the 3D distance between the fighter and bomber planes
    distance = math.sqrt((xf - xb) ** 2 + (yf - yb) ** 2 + (zf - zb) ** 2)

    if distance <= 100:
        print("The Bomber Plane Shot Down at time", time)
        print(f"\nPursuit ends, shot at {time} minutes and at {distance:.2f} km.")
        flag = 1
    elif distance > 1000:
        print("The Bomber Plane Escapes at time", time)
        print(f"\nPursuit ends, escape at {time} minutes and at {distance:.2f} km.")
        flag = 1
    else:
        # Update the fighter plane's position in 3D towards the bomber
        xf += vf * (xb - xf) / distance
        yf += vf * (yb - yf) / distance
        zf += vf * (zb - zf) / distance

        # Randomly update bomber's 3D position
        xb, yb, zb = random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)
        time += 1
