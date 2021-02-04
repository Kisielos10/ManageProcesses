from algorithms.fcfs import *
from algorithms.lcfs import *
from algorithms.fifo import *
from algorithms.lru import *
from algorithms.sjf import *

from process.schedule_process import *
from process.page_process import *

process_list = []

# generate data to process
generate_processes(process_list)
# schedule and execute processes
fcfs(process_list)

lcfs(process_list)

sjf(process_list)

sjf(process_list)

# clear the list fill it with new processes
process_list.clear()
# number of pages for page replacement algorithm
pages = 3
# generate data to process
generate_page_processes(process_list)
# schedule and execute page processes
fifo(process_list, pages)

lru(process_list, pages)

print("Done")
