def write_from_page(page, file_name, number):
    """
    Generate a visualization of how the algorithm works
    :param page: int
        number of page
    :param file_name: string
        name of the file
    :param number: int
        data in process
    :return:
        write to file
    """
    file = open(file_name, 'a')
    for i in range(len(page)):
        file.write('[ ' + str(page[i]) + ' ]')
    file.write("\t" + str(number) + "\n")


def generate_page_stats(file_name, process_list, page_hits):
    """
    Generate a statistics to file
    :param file_name: string
        name of the file
    :param process_list: list
        list of integers that simulate data
    :param page_hits: int
        page replacement algorithm "hits"
    :return:
        write statistics to file
    """
    file = open(file_name, 'a')
    file.write(
        'Page Hits: {}\nPage Faults: {}\nPage Hit Ratio {}%\nPage Fault Ratio: {}%'.format(
            page_hits,
            len(process_list) - page_hits,  # page faults
            round((page_hits / len(process_list)) * 100),  # page hit ratio
            round(((len(process_list) - page_hits) / len(process_list)) * 100)))  # page fault ratio
