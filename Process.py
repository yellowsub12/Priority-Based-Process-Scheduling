class Process:
    def __init__(self, id, arrival_time,burst,priority,nb_executions):
        self.id = id
        self.arrival_time = arrival_time
        self.burst = burst
        self.priority = priority
        self.nb_excutions = nb_executions


    def time_slot(self):
        if self.priority < 100:
            slot = (140 - self.priority) * 0.020 
        else:
            slot = (140 - self.priority) * 0.005
        return slot   

    def time_slot(self, a):
        if a < 100:
            slot = (140 - a) * 0.020 
        else:
            slot = (140 - a) * 0.005
        return slot            


    def print(self):
        print("id is: " + str(self.id))
        print("Arrival time is: " + str(self.arrival_time))
        print("burst: " + str(self.burst))
        print("Priority is: " + str(self.priority))

<<<<<<< Updated upstream

    def getID(self):
        return self.id
=======
    def getArrivalTime(self):
        return self.arrival_time

    def setNumberExecution(self):
        self.nb_excutions = self.nb_excutions + 1

    def setNumberExecution(self, a):
        self.nb_excutions = a

    def getNumberExecution(self):
       return self.nb_excutions

    def getBurst(self):
        return self.burst

    def setBurst(self, a):
        self.burst = a
>>>>>>> Stashed changes
