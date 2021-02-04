from statistic.schedule_statistic import *


def fcfs(process_list):
    """
    implementation of First Come First Serve algorithm as a simulation
    :param process_list: list
        list containing objects of Process class
    :return:
        sortable list of processes
    """
    queue = []
    # simulation of a processor clock rate
    cpu_clock = 0
    queue += (x for x in process_list if x.arrival == cpu_clock)
    counter = 0
    while counter < len(process_list):
        if len(queue) != 0:
            queue[0].set_response_time(cpu_clock, int(getattr(queue[0], "arrival")))
            queue[0].set_turnaround_time(int(getattr(queue[0], "burst")), int(getattr(queue[0], "response_time")))
            for burst in range(int(getattr(queue[0], "burst"))):
                cpu_clock += 1
                queue += (x for x in process_list if x.arrival == cpu_clock)
            counter += 1
            queue.pop(0)
        else:
            cpu_clock += 1
            queue += (x for x in process_list if x.arrival == cpu_clock)
    # generate statistics
    generate_stats(process_list, "fcfs.txt")
