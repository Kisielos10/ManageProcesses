def generate_stats(process_list, file_name):
    """
        Generate a statistics to file
    :param process_list: list
        list containing objects of Process class
    :param file_name: string
        name of the file
    :return:
        generate statistics of the algorithm
    """
    # sort algorithms by response time after they have been processed
    process_list.sort(key=lambda x: x.turnaround_time, reverse=False)
    file = open(file_name, 'w')
    for process in process_list:
        file.write(
            '{}.\n Burst Time: {}\n Arrival Time: {} \n Response Time: {} \n Turnaround Time: {}\n'.format(
                process.number
                , process.burst
                , process.arrival
                , process.response_time
                , process.turnaround_time))

    file.write(
        'Average process response time: {}\nAverage process turnaround time: {}'.format(
            sum([obj.response_time for obj in process_list]) / len(process_list),
            sum([obj.turnaround_time for obj in process_list]) / len(process_list)))
    # clear data in order to let other processes write and read from it
    for process in process_list:
        process.response_time = 0
        process.waiting_time = 0
        process.turnaround_time = 0
