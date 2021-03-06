from statistic.schedule_statistic import *


def lcfs(process_list):
    """
    implementation of Last Come First Serve algorithm as a simulation
    :param process_list: list
        list containing objects of Process class
    :return:
        sortable list of processes
    """
    # process queue
    queue = []
    # simulation of a processor clock rate
    cpu_clock = 0
    # insert in to queue processes that arrive at time 0
    queue += (x for x in process_list if x.arrival == cpu_clock)
    counter = 0

    while counter < len(process_list):
        if len(queue) != 0:
            current_process = queue[-1]
            current_process.set_response_time(cpu_clock, int(getattr(current_process, "arrival")))
            current_process.set_turnaround_time(int(getattr(current_process, "burst")),
                                                int(getattr(current_process, "response_time")))
            for burst in range(int(getattr(current_process, "burst"))):
                cpu_clock += 1
                queue += (x for x in process_list if x.arrival == cpu_clock)

            counter += 1
            queue.pop(queue.index(current_process))
        else:
            cpu_clock += 1
            queue += (x for x in process_list if x.arrival == cpu_clock)
    # generate statistics
    generate_stats(process_list, "lcfs.txt")
