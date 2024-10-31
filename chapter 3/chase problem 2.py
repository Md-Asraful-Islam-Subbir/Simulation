import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


# Initialize positions
a = [10, 10]
b = [30, 10]
c = [30, 30]
d = [10, 30]

# Initialize velocities
va = 35
vb = 25
vc = 15
vd = 10

# Initialize time and time increment
time = 0
delt = 0.01

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(0, 40)
ax.set_aspect('equal')
ax.set_title("Chase Animation with Curved Paths")
ax.set_xlabel("X position")
ax.set_ylabel("Y position")

# Initialize scatter plots for each point
point_a, = ax.plot([], [], 'bo', label="A")
point_b, = ax.plot([], [], 'ro', label="B")
point_c, = ax.plot([], [], 'go', label="C")
point_d, = ax.plot([], [], 'mo', label="D")

# Lines to show paths of each point
path_a, = ax.plot([], [], 'b--', lw=1)
path_b, = ax.plot([], [], 'r--', lw=1)
path_c, = ax.plot([], [], 'g--', lw=1)
path_d, = ax.plot([], [], 'm--', lw=1)

# Track the path of each point
a_path_x, a_path_y = [a[0]], [a[1]]
b_path_x, b_path_y = [b[0]], [b[1]]
c_path_x, c_path_y = [c[0]], [c[1]]
d_path_x, d_path_y = [d[0]], [d[1]]

# Text to display time
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)


# Initialization function
def init():
    point_a.set_data([], [])
    point_b.set_data([], [])
    point_c.set_data([], [])
    point_d.set_data([], [])
    path_a.set_data([], [])
    path_b.set_data([], [])
    path_c.set_data([], [])
    path_d.set_data([], [])
    time_text.set_text('')
    return point_a, point_b, point_c, point_d, path_a, path_b, path_c, path_d, time_text


# Update function for animation
def update(frame):
    global a, b, c, d, time

    # Calculate distances between points
    distance_AB = distance(a, b)
    distance_BC = distance(b, c)
    distance_CD = distance(c, d)
    distance_DA = distance(d, a)

    # Update positions
    a[0] += va * delt * (b[0] - a[0]) / distance_AB
    a[1] += va * delt * (b[1] - a[1]) / distance_AB
    b[0] -= vb * delt * (b[0] - c[0]) / distance_BC
    b[1] += vb * delt * (c[1] - b[1]) / distance_BC
    c[0] -= vc * delt * (c[0] - d[0]) / distance_CD
    c[1] -= vc * delt * (c[1] - d[1]) / distance_CD
    d[0] += vd * delt * (a[0] - d[0]) / distance_DA
    d[1] += vd * delt * (a[1] - d[1]) / distance_DA

    # Update paths
    a_path_x.append(a[0])
    a_path_y.append(a[1])
    b_path_x.append(b[0])
    b_path_y.append(b[1])
    c_path_x.append(c[0])
    c_path_y.append(c[1])
    d_path_x.append(d[0])
    d_path_y.append(d[1])

    # Update scatter points for each object
    point_a.set_data([a[0]], [a[1]])
    point_b.set_data([b[0]], [b[1]])
    point_c.set_data([c[0]], [c[1]])
    point_d.set_data([d[0]], [d[1]])

    # Update path lines
    path_a.set_data(a_path_x, a_path_y)
    path_b.set_data(b_path_x, b_path_y)
    path_c.set_data(c_path_x, c_path_y)
    path_d.set_data(d_path_x, d_path_y)

    # Update time text
    time_text.set_text(f'Time: {time:.2f}s')

    # Check for collisions
    if distance_AB < 0.005:
        print("A hits B")
        ani.event_source.stop()
    elif distance_BC < 0.005:
        print("B hits C")
        ani.event_source.stop()
    elif distance_CD < 0.005:
        print("C hits D")
        ani.event_source.stop()
    elif distance_DA < 0.005:
        print("D hits A")
        ani.event_source.stop()

    # Increase the time
    time += delt

    return point_a, point_b, point_c, point_d, path_a, path_b, path_c, path_d, time_text


# Create animation
ani = animation.FuncAnimation(fig, update, frames=1000, init_func=init, interval=20, blit=True)

# Display legend and show plot
ax.legend()
plt.show()
