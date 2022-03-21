class Process:
    def __init__(self, id, arrival_time,burst,priority,nb_executions):
        self.id = id
        self.arrival_time = arrival_time
        self.burst = burst
        self.priority = priority
        self.nb_excutions = nb_executions
        self.update_execution = 0
        self.waiting_time = 0


    def time_slot(self):
        if int(self.priority) < 100:
            slot = (140 - int(self.priority)) * 20 
        else:
            slot = (140 - int(self.priority)) * 5
        return slot   

    def time_slot2(self, a):
        if int(a) < 100:
            slot = (140 - int(a)) * 20 
        else:
            slot = (140 - int(a)) * 5
        return slot            


    def print(self):
        print("id is: " + str(self.id))
        print("Arrival time is: " + str(self.arrival_time))
        print("burst: " + str(self.burst))
        print("Priority is: " + str(self.priority))

    def getArrivalTime(self):
        return self.arrival_time

    def setNumberExecution(self):
        if self.nb_excutions <= 2:
            self.nb_excutions = self.nb_excutions + 1
        else:
            self.nb_execution = 0

    def getNumberExecution(self):
       return self.nb_excutions

    def getBurst(self):
        return self.burst

    def setBurst(self, a):
        self.burst = a

    def getNbUpdate(self):
        return self.update_execution

    def setNbUpdate(self, a):
        self.update_execution = a

    def getWaiting(self):
        return self.waiting_time

    def setWaiting(self, a):
        self.waiting_time = self.waiting_time + a

    def getID(self):
        return self.id

    def setPriority(self, a):
        self.priority = a
        self.time_slot2(self.priority)

    def getPriority(self):
        return self.priority