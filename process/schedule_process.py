from random import uniform
from helper_class.process_class import *


def generate_processes(process_list, process_count=100, start=0, end=20):
    """
    Generates tmp_a processes burst and arrival times & saves to file
    :param process_count: int
        number of processes
    :param start: int
        the first number that can be generated
    :param end: int
        the last number that can be generated
    :param process_list: list
        list containing objects of Process class
    :return:
        save to file
    """

    # gets ordinal number
    counter = 1
    file = open("process_file.txt", 'w')

    for line in range(process_count):
        items = [counter, round(uniform(start, end)) + 1, round(uniform(start, end))]
        # save to file
        file.write(','.join([str(element) for element in items]) + '\n')
        # use parametrized constructor
        process = Process(counter, items[1], items[2])
        process_list.append(process)
        counter += 1
