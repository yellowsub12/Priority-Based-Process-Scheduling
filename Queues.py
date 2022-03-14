import queue

class Queues:
    def __init__(self, a, b):
        queue1 = a
        queue2 = b
        flag1 = False
        flag2 = True

    def flag_update(self, a, b): #a and b are booleans
        self.flag1 = a
        self.flag2 = b

    def put(self, a, parameter): #a is the queue number, parameter is the process to be passed to the queue
        if a == 1:
            self.queue1.put(parameter)
        else:
            self.queue2.put(parameter)

    def get(self, a, parameter): #a is the queue number, parameter is the process to be poped off the queue
        if a == 1:
            self.queue1.get(parameter)
        else:
            self.queue2.get(parameter)
            
    def print(self):
        for s in self.queue1.queue:
            print(s)
        for i in self.queue2.queue:
            print(i)
        


