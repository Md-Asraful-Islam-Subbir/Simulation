#c1 = [50.0]
#c2 = [25.0]
#c3 = [0.0]
#kl = 0.025
#k2 = 0.01
#time_difference = 0.1
#t = 0.0
#last_time = 15.0
#i = 0
# Get user input for initial concentrations and constants
c1 = [float(input("Enter the initial concentration of C1: "))]
c2 = [float(input("Enter the initial concentration of C2: "))]
c3 = [float(input("Enter the initial concentration of C3: "))]
kl = float(input("Enter the reaction rate constant kl: "))
k2 = float(input("Enter the reaction rate constant k2: "))
time_difference = float(input("Enter the initial time step size: "))
last_time = float(input("Enter the final time for the simulation: "))

t = 0.0
i = 0

# Print header for results
print("\nTime  \tC1    \tC2    \tC3")

# Start the simulation
while t <= last_time:
    print(f"{t:.2f} \t{c1[i]:.2f} \t{c2[i]:.2f} \t{c3[i]:.2f}")

    # Calculate next concentrations
    c1_next = c1[i] + (k2 * c3[i] - kl * c1[i] * c2[i]) * time_difference
    c2_next = c2[i] + (k2 * c3[i] - kl * c1[i] * c2[i]) * time_difference
    c3_next = c3[i] + 2.0 * (kl * c1[i] * c2[i] - k2 * c3[i]) * time_difference

    # Append the next values
    c1.append(c1_next)
    c2.append(c2_next)
    c3.append(c3_next)

    # Update time and index
    i += 1
    t += time_difference

    # Adjust time step at specific times
    if t >= 2.0 and time_difference < 0.2:
        time_difference = 0.2
    if t >= 6.0 and time_difference < 0.4:
        time_difference = 0.4
