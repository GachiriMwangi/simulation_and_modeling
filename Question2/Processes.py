import math
import random 

# Constants
Q_LIMIT = 100
BUSY = 1
IDLE = 0
num_events = 2

# Global variables
next_event_type = 0
num_custs_delayed = 0
num_delays_required = 0
num_in_q = 0
server_status = IDLE
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [0.0] * 3
total_of_delays = 0.0
area_num_in_q = 0.0
area_server_status = 0.0

# Function to initialize simulation
def initialize():
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30

# Function to determine next event type
def timing():
    global sim_time, next_event_type
    min_time_next_event = min(time_next_event[1:num_events + 1])
    next_event_type = time_next_event.index(min_time_next_event)

    sim_time = min_time_next_event

# Function to handle arrival event
def arrive():
    global sim_time, server_status, num_in_q, total_of_delays, num_custs_delayed
    delay = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            print("\nOverflow of the array time_arrival at time", sim_time)
            exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)

# Function to handle departure event
def depart():
    global sim_time, server_status, num_in_q, total_of_delays, num_custs_delayed
    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]

# Function to generate exponential variate
def expon(mean):
    return -mean * math.log(random.random())

# Function to generate simulation report
def report(outfile):
    print("Single Server Queuing System.", file=outfile)
    print("\nAverage delay in queue", "{:.4f}".format(total_of_delays / num_custs_delayed), file=outfile)
    print("Average number in queue", "{:.4f}".format(area_num_in_q / sim_time), file=outfile)
    print("Server utilization", "{:.4f}".format(area_server_status / sim_time), file=outfile)
    print("Time simulation ended", "{:.4f}".format(sim_time), file=outfile)

# Function to update time average statistics
def update_time_avg_stats():
    global sim_time, time_last_event, area_num_in_q, area_server_status
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

if __name__ == "__main__":
    infile = open("mm1.in", "r")
    outfile = open("mm1.out", "w")
    num_events = 2
    mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())

    initialize()

    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()

        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()

    report(outfile)

    infile.close()
    outfile.close()
