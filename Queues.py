class Queues:
    def __init__(self):
        queue1 = []
        queue2 = []
        flag1 = False
        flag2 = True

    def flag_update(self, a, b): #a and b are booleans
        self.flag1 = a
        self.flag2 = b

    def push(self, a, parameter): #a is the queue number, parameter is the process to be passed to the queue
        if a == 1:
            self.queue1.append(parameter)
        else:
            self.queue2.append(parameter)

    def pop(self, a, parameter): #a is the queue number, parameter is the process to be poped off the queue
        if a == 1:
            self.queue1.pop(parameter)
        else:
            self.queue2.pop(parameter)
        


