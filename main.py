from hashlib import new
from multiprocessing.connection import wait
from Process import Process
import queue
import time
import threading
import os
import math

def read_file():
    open_file = open("input.txt", "r")
    lines = []
    for line in open_file:
        lines.append(line)
    open_file.close()
    return lines

def create_processes(array):
    global nb_processes 
    nb_processes = int(array[0])
    new_array = array[1:]
    return_array = []
    count = 0
    previous_time = 0
    temp = 0

    for i in new_array:
        i = new_array[count]
        x = i.split()
        pid = x[0]
        arr_time = int(x[1])
        burst = int(x[2])
        priority = x[3]
        process = Process(pid,arr_time,burst,priority)
        if arr_time < previous_time and 1 < count:
            temp = return_array.pop(count-1)
            return_array.insert(count - 1, process)
            return_array.append(temp)
        else:
            return_array.append(process)
        previous_time = arr_time
        count = count + 1
        if count == len(new_array):
            break
    return return_array

def updates(process, waiting_time):
    old_priority = process.getPriority() 
    bonus = math.floor((10*waiting_time)/(clock - process.getArrivalTime()))
    new_priority = max(100,min((int(old_priority) - int(bonus) + 5), 139))
    return new_priority


def waiting_times(process, clock):
    if process.getNbUpdate() == 0:
        temp = clock - process.getLastExecution() - process.getArrivalTime()
        process.setWaiting(temp)
        print("Hello" + str(temp))
        process.setNbUpdate(1)
        print(str(process.getNbUpdate()))
    else:
        process.setWaiting((clock - process.getLastExecution())) 
    return process.getWaiting()

interval = 1
clock = 1000 


def main():
    threading.Timer(interval, main).start()
    main_function_2()


def main_function_2():
    global flag1
    global flag2
    global clock
    global count_processes
    clock = clock + 1000
    expired_processes = []
    print("Clock is %d" % clock)

    while True:

        if count_processes < nb_processes:
            x = processes[count_processes] #initialize the new processes
            if x.getArrivalTime() <= clock : #current time of the clock:
                if flag1 == True:
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    queue2.put(x)
                    count_processes = count_processes + 1
                else:
                    print("Time " + str(x.getArrivalTime()) + ", " + str(x.getID()) + ", Arrived")
                    queue1.put(x)
                    count_processes = count_processes + 1

        if flag1 == True and queue1.empty():
                flag1 = False
                flag2 = True
        elif flag2 == True and queue2.empty():
                flag1 = True
                flag2 = False
    
    
        #execute time slot
        if flag1 == True:
            execution = queue1.get()
            print("Time " + str(clock) + ", " + str(execution.getID()) + ", Started, Granted " + str(execution.time_slot()))
            wait_time = waiting_times(execution, clock)
            if execution.time_slot() < execution.getBurst():
                print(execution.getNumberExecution())
                clock = clock + execution.time_slot()
                execution.setLastExecution(clock)
                temp = (execution.getBurst() - execution.time_slot())
                execution.setBurst(temp)
                execution.setNumberExecution() #update the number of times this process has executed in a row
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Paused")
                if execution.getNumberExecution() % 2 == 0:
                    print(wait_time)
                    execution.setPriority(updates(execution, wait_time))
                    print("Time " + str(clock) + ", " + str(execution.getID()) + ", Priority updated to " +  str(execution.getPriority()))
                queue2.put(execution)
            else:
                clock = clock + execution.time_slot()
                execution.setBurst(0) # process is finished
                expired_processes.append(execution)
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Finished")
                continue
        else:
            execution = queue2.get()
            print("Time " + str(clock) + ", " + str(execution.getID()) + ", Started, Granted " + str(execution.time_slot()))
            wait_time = waiting_times(execution, clock)
            if execution.time_slot() < execution.getBurst():
                print(execution.getNumberExecution())
                clock = clock + execution.time_slot()
                execution.setLastExecution(clock)
                temp = (execution.getBurst() - execution.time_slot())
                execution.setBurst(temp)
                execution.setNumberExecution() #update the number of times this process has executed in a row
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Paused")
                if execution.getNumberExecution() % 2 == 0:
                    print(wait_time)
                    execution.setPriority(updates(execution, wait_time))
                    print("Time " + str(clock) + ", " + str(execution.getID()) + ", Priority updated to " +  str(execution.getPriority()))
                queue1.put(execution)
            else:
                clock = clock + execution.time_slot()
                execution.setBurst(0) # process is finished
                expired_processes.append(execution)
                print("Time " + str(clock) + ", " + str(execution.getID()) + ", Finished")
                continue

        if len(expired_processes) > nb_processes - 1:
            print("test test")
            os.exit()

if __name__ == "__main__":
    flag1 = True     #queue1 flag
    flag2 = False #queue2 flag
    clock = 0
    start_time = time.time()
    queue1 = queue.Queue()
    queue2 = queue.Queue()
    pass1 = read_file()
    processes = create_processes(pass1)
    count_processes = 0
    main()