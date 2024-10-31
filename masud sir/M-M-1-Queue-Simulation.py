import numpy as np
import queue
import copy
import matplotlib.pyplot as plt

# Input Parameters
total_time = int(input("Enter total simulation time (Hours): "))
IAT_rate = int(input("Enter Mean Inter Arrival Time (Jobs/Hour): "))
ST_rate = int(input("Enter Mean Service Time (Jobs/Hour): "))
max_customers = int(input("Enter maximum number of customers: "))

# Initialize Parameters
qu = queue.Queue()
curr_process = None
IAT = []
ST = []
AT = []
wait_time = []
server_busy = False
list_wait = []
list_delay = []
list_queue_len = []
num_processes_served = 0
num_in_queue = 0
time_simulation_ended = 0

# Populate Inter-Arrival-Times (IAT)
for i in range(max_customers):
    temp = np.random.exponential(1 / IAT_rate) * 60 * 60
    if i == 0:
        IAT.append(0)
    else:
        IAT.append(int(temp))

# Populate Service-Times (ST) (where ST[i] != 0)
while len(ST) < max_customers:
    temp = np.random.exponential(1 / ST_rate) * 60 * 60
    if temp > 0:
        ST.append(int(temp))

# Save a copy of ST
ST_copy = copy.deepcopy(ST)

# Get Arrival-Times (AT) from IAT starting at t=0 and initialize Waiting-Times to 0
for i in range(max_customers):
    if i == 0:
        AT.append(0)
    else:
        AT.append(AT[i - 1] + IAT[i])
    wait_time.append(0)

# Simulation of M/M/1 Queue
for t in range(total_time * 60 * 60):  # Simulation runs in seconds
    if server_busy:
        # Reduce service time for current process and increase wait times for others in queue
        ST[curr_process] -= 1
        for item in list(qu.queue):
            wait_time[item] += 1

        if ST[curr_process] == 0:  # When service is finished for the current process
            server_busy = False
            num_processes_served += 1
            if num_processes_served == max_customers:
                time_simulation_ended = t
                break

    # Check for customer arrivals at the current time
    for j in range(max_customers):
        if t == AT[j]:
            qu.put(j)

    # Start serving a process if the server is not busy
    if not server_busy and not qu.empty():
        curr_process = qu.get()
        server_busy = True

    # Keep track of the number in queue
    num_in_queue = qu.qsize()
    list_queue_len.append(num_in_queue)

    # Calculate average wait and delay
    sum_wait = sum(wait_time[:num_processes_served]) if num_processes_served > 0 else 0
    sum_delay = sum([wait_time[i] + ST_copy[i] for i in range(num_processes_served)]) if num_processes_served > 0 else 0

    if num_processes_served > 0:
        list_wait.append(sum_wait / (num_processes_served * 60 * 60))  # Convert seconds to hours
        list_delay.append(sum_delay / (num_processes_served * 60 * 60))  # Convert seconds to hours
    else:
        list_wait.append(0)
        list_delay.append(0)

# Plot results
plt.plot(range(len(list_wait)), list_wait)
plt.ylabel("Avg Wait Time (Hours)")
plt.xlabel("Time (Seconds)")
plt.show()

plt.plot(range(len(list_delay)), list_delay)
plt.ylabel("Avg Delay Time (Hours)")
plt.xlabel("Time (Seconds)")
plt.show()

plt.plot(range(len(list_queue_len)), list_queue_len)
plt.ylabel("Number in Queue")
plt.xlabel("Time (Seconds)")
plt.show()

# Calculate the total service time used
total_service_time = sum(ST_copy[:num_processes_served])

# Server utilization: proportion of time the server is busy
server_utilization = total_service_time / (total_time * 60 * 60)  # Convert time to seconds

# Calculate average queue length
average_queue_length = sum(list_queue_len) / len(list_queue_len)

# Calculate average wait time and average delay time
average_wait_time = sum(list_wait) / len(list_wait)
average_delay_time = sum(list_delay) / len(list_delay)

# Display Results
print(f"Average Wait Time: {average_wait_time:.4f} hours")
print(f"Average Delay Time: {average_delay_time:.4f} hours")
print(f"Average Number in Queue: {average_queue_length:.2f}")
print(f"Server Utilization: {server_utilization:.2f}")
print(f"Time Simulation Ended: {time_simulation_ended / 60:.2f} minutes")
