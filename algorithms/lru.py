from statistic.page_statistic import *


def lru(process_list, pages):
    """
    implementation of Least Recently Used page replacement algorithm as a simulation
    :param process_list: list
        list containing objects of Process class
    :param pages: int
        number of pages for page replacement algorithm
    :return:
        generation of visualization and statistics
    """
    # create a file if it hasn't been already created or clear it
    open("lru.txt", 'w')
    page_hits = 0
    # current page content
    page = []
    # list representing "time" since last usage
    helper_list = []
    # variable containing the index of the least recently used packet
    least_recently_used = 0
    for number in process_list:
        if any(element == number for element in page):
            page_hits += 1
            helper_list[page.index(number)] = 0
        else:
            if len(page) < pages:
                page.append(number)
                helper_list.append(0)
            else:
                page[least_recently_used] = number
                helper_list[least_recently_used] = 0
        for i in range(len(page)):
            helper_list[i] += 1
        least_recently_used = helper_list.index(max(helper_list))
        write_from_page(page, "lru.txt", number)
    # generate statistics
    generate_page_stats("lru.txt", process_list, page_hits)
