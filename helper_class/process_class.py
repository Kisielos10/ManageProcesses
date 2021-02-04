class Process:
    """
        Process class definition
        Methods:
            set_response_time(): set process response time
            set_turnaround_time(): set process turnaround time
            set_waiting_time(): set process waiting time
        Attributes:
            number: int
                ordinal number
            burst: int
                process execution time
            arrival: int
                time of process arrival
            response_time: int
                time in which the process gets the CPU for the first time
            waiting_time: int
                time spent in the queue
            turnaround_time: int
                time spent in the queue + burst time
    """
    number = 0
    burst = 0
    arrival = 0
    response_time = 0
    turnaround_time = 0

    def __init__(self, number, burst, arrival):
        """
        Create a process object
        :param number: int
            ordinal number
        :param burst: int
            process execution time
        :param arrival: int
            time of process arrival
        """
        self.number = number
        self.burst = burst
        self.arrival = arrival

    def set_response_time(self, x, y):
        self.response_time = x - y

    def set_turnaround_time(self, x, y):
        self.turnaround_time = x + y

