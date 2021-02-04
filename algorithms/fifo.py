from statistic.page_statistic import *


def fifo(process_list, pages):
    """
    implementation of First In First Out page replacement algorithm as a simulation
    :param process_list: list
        list containing objects of Process class
    :param pages: int
        number of pages for page replacement algorithm
    :return:
        generation of visualization and statistics
    """
    # create a file if it hasn't been already created or clear it
    open("fifo.txt", 'w')
    # current page content
    page = []
    page_hits = 0
    current_index = 0
    for number in process_list:
        if any(element == number for element in page):
            page_hits += 1
        else:
            if len(page) < pages:
                page.append(number)
            else:
                page[current_index] = number
            current_index += 1
            if current_index == pages:
                current_index = 0
        write_from_page(page, "fifo.txt", number)
    # generate statistics
    generate_page_stats("fifo.txt", process_list, page_hits)
