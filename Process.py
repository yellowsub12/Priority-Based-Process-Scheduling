class Process:
    def __init__(self, id, arrival_time,burst,priority):
        self.id = id
        self.arrival_time = arrival_time
        self.burst = burst
        self.priority = priority


    def time_slot(self):
        if self.priority < 100:
            slot = (140 - self.priority) * 0.020 
        else:
            slot = (140 - self.priority) * 0.005
        return slot            


    def print(self):
        print("id is: " + str(self.id))
        print("Arrival time is: " + str(self.arrival_time))
        print("burst: " + str(self.burst))
        print("Priority is: " + str(self.priority))