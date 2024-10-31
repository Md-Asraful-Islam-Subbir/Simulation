import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fighter's speed (km/min) and maximum pursuit time (minutes)
vf = 20  # Fighter speed in km/min
max_time = 12  # Maximum pursuit time in minutes
shot_distance = 10  # Distance within which missile can be fired (km)

# Initial positions of the fighter and bomber planes
xf, yf = 0, 50
xb = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219, 226, 234, 240]
yb = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23, 19, 16, 14]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-50, 300)
ax.set_ylim(-50, 100)
ax.set_title("Fighter Pursuit of Bomber")
ax.set_xlabel("X position (km)")
ax.set_ylabel("Y position (km)")

# Initialize the plot elements
fighter_dot, = ax.plot([], [], 'bo', label="Fighter")
bomber_dot, = ax.plot([], [], 'ro', label="Bomber")
shot_line, = ax.plot([], [], 'k--', lw=1.5)
text = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha="center")

# Lines to show the paths of fighter and bomber
fighter_path_line, = ax.plot([], [], 'b-', lw=1, label="Fighter Path")
bomber_path_line, = ax.plot([], [], 'r-', lw=1, label="Bomber Path")

# Track the path of the fighter and bomber
fighter_path_x, fighter_path_y = [xf], [yf]
bomber_path_x, bomber_path_y = [], []

# Initialize the plot elements for animation
def init():
    fighter_dot.set_data([], [])
    bomber_dot.set_data([], [])
    shot_line.set_data([], [])
    fighter_path_line.set_data([], [])
    bomber_path_line.set_data([], [])
    text.set_text("")
    return fighter_dot, bomber_dot, shot_line, fighter_path_line, bomber_path_line, text

# Update function for animation
def update(frame):
    global xf, yf
    xb_current = xb[frame]
    yb_current = yb[frame]
    bomber_path_x.append(xb_current)
    bomber_path_y.append(yb_current)

    # Calculate distance between fighter and bomber
    distance = math.sqrt((xf - xb_current) ** 2 + (yf - yb_current) ** 2)

    # Print details for each frame in the console
    print(f"Minute {frame + 1}: Fighter at ({xf:.2f}, {yf:.2f}), "
          f"Bomber at ({xb_current}, {yb_current}), Distance = {distance:.2f} km")

    # Check if within shooting range
    if distance <= shot_distance:
        print(f"Shooting! Bomber Shot Down at {frame + 1} minutes.")
        text.set_text(f"Shooting! Bomber Shot Down at {frame + 1} minutes.")
        shot_line.set_data([xf, xb_current], [yf, yb_current])  # Draw line showing the "shot"
        fighter_dot.set_data([xf], [yf])  # Use lists for single points
        bomber_dot.set_data([xb_current], [yb_current])  # Use lists for single points
        fighter_path_line.set_data(fighter_path_x, fighter_path_y)
        bomber_path_line.set_data(bomber_path_x, bomber_path_y)

        # Stop the animation when the bomber is shot down
        ani.event_source.stop()
        return fighter_dot, bomber_dot, shot_line, fighter_path_line, bomber_path_line, text

    # Calculate direction
    sin_theta = (yb_current - yf) / distance
    cos_theta = (xb_current - xf) / distance

    # Update fighter's position
    xf += vf * cos_theta
    yf += vf * sin_theta

    # Update paths
    fighter_path_x.append(xf)
    fighter_path_y.append(yf)

    # Update plot elements
    fighter_dot.set_data([xf], [yf])  # Use lists for single points
    bomber_dot.set_data([xb_current], [yb_current])  # Use lists for single points
    fighter_path_line.set_data(fighter_path_x, fighter_path_y)  # Update fighter path
    bomber_path_line.set_data(bomber_path_x, bomber_path_y)  # Update bomber path
    shot_line.set_data([], [])  # Clear shot line until within range
    text.set_text(f"Minute {frame + 1}: Distance = {distance:.2f} km")

    return fighter_dot, bomber_dot, shot_line, fighter_path_line, bomber_path_line, text

# Create animation
ani = animation.FuncAnimation(fig, update, frames=min(max_time, len(xb)),
                              init_func=init, blit=True, interval=500, repeat=False)

# Display legend and show plot
ax.legend()
plt.show()
