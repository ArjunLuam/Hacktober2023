from collections import deque

class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time

def round_robin_scheduling(processes, quantum):
    queue = deque(processes)
    while queue:
        current_process = queue.popleft()
        if current_process.burst_time <= quantum:
            print(f"Executing {current_process.name} for {current_process.burst_time} units")
            current_process.burst_time = 0
        else:
            print(f"Executing {current_process.name} for {quantum} units")
            current_process.burst_time -= quantum
        if current_process.burst_time > 0:
            queue.append(current_process)

if __name__ == "__main__":
    processes = [
        Process("P1", 10),
        Process("P2", 5),
        Process("P3", 8),
        Process("P4", 2)
    ]
    quantum = 2
    round_robin_scheduling(processes, quantum)
