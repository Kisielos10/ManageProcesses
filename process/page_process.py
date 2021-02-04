from random import uniform


def generate_page_processes(process_list, process_count=10, start=1, end=10):
    """
    Generates random processes & saves to file
    :param process_count: int
        number of processes
    :param start: int
        the first number that can be generated
    :param end: int
        the last number that can be generated
    :param process_list: list
        list containing objects of Process class
    :return
        save to file
    """
    for i in range(process_count):
        process_list.append(round(uniform(start, end)))
    file = open("page_process_file.txt", 'w')
    # save to file
    file.write(','.join(([str(element) for element in process_list])))
