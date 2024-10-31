import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravitational acceleration (m/s^2)
c = 0.01  # Drag coefficient (this value is assumed for example)
m = 1.0  # Mass of the cannonball (kg)


# Function to compute the range based on initial conditions
def compute_range(v0, theta0, dt=0.01):
    # Initial conditions
    x, y = 0, 0  # Initial position (m)
    theta = np.radians(theta0)  # Convert angle to radians
    vx = v0 * np.cos(theta)  # Initial x velocity
    vy = v0 * np.sin(theta)  # Initial y velocity

    # Run the simulation until the cannonball hits the ground (y <= 0)
    while y >= 0:
        # Calculate speed
        v = np.sqrt(vx ** 2 + vy ** 2)

        # Update velocities (using the drag force proportional to v^2)
        vx += (-c * v * vx / m) * dt
        vy += (-g - (c * v * vy / m)) * dt

        # Update positions
        x += vx * dt
        y += vy * dt

    return x  # Final range when y <= 0


# Generating a range table for various muzzle velocities and angles
muzzle_velocities = np.linspace(50, 300, 6)  # Example velocities from 50 to 300 m/s
angles = np.linspace(10, 80, 8)  # Example angles from 10 to 80 degrees

# Table for ranges
print("Range Table (m):")
print(f"{'Velocity (m/s)':<15}{'Angle (degrees)':<15}{'Range (m)':<15}")
print("-" * 45)
for v0 in muzzle_velocities:
    for theta0 in angles:
        range_value = compute_range(v0, theta0)
        print(f"{v0:<15.2f}{theta0:<15.2f}{range_value:<15.2f}")

# Plotting the range as a function of muzzle velocity and angle
plt.figure(figsize=(10, 6))
for theta0 in angles:
    ranges = [compute_range(v0, theta0) for v0 in muzzle_velocities]
    plt.plot(muzzle_velocities, ranges, label=f"{theta0}°")

plt.xlabel("Muzzle Velocity (m/s)")
plt.ylabel("Range (m)")
plt.title("Range vs. Muzzle Velocity for Various Angles")
plt.legend(title="Angle")
plt.grid(True)
plt.show()
