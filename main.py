from hashlib import new
from multiprocessing.connection import wait
from Process import Process
import queue
import time
import threading
import os

def read_file():
    open_file = open("input.txt", "r")
    lines = []
    for line in open_file:
        lines.append(line)
    open_file.close()
    return lines

def create_processes(array):
    global nb_processes 
    nb_processes = array[0]
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
        process = Process(pid,arr_time,burst,priority,0)
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

#def updates():
#    waiting_time = sum_of_waiting_times
#    bonus = 10*waiting_time/(clock - arrival_time)
#    new_priority = max(100,min(old_priority - bonus + 5139))
#   return new_priority     this value is to be passes to the time slot function of the process so the priority updates


interval = 1
clock = 0 


def main():
    threading.Timer(interval, main).start()
    main_function_2()


def main_function_2():
    global flag1
    global flag2
    global clock
    global count_processes
    clock = clock + 1000
    print("Clock is %d" % clock)

    while True:
        #Is the active queue empty
        if flag1 == True and queue1.empty():
            flag1 = False
            flag2 = True
        elif flag2 == True and queue2.empty():
            flag1 = True
            flag2 = False

        x = processes[count_processes] #initialize the new processes
        if x.getArrivalTime() == clock : #current time of the clock:
            if flag1 == True:
                queue2.put(x)
                count_processes = count_processes + 1
                flag2 = True
                flag1 = False
            else:
                queue1.put(x)
                count_processes = count_processes + 1
                flag1 = True
                flag2 = False

    
    
        #execute time slot
        if flag1 == True:
            process_start_time = clock
            execution = queue1.get()
            if 1000 < execution.getBurst():
                execution.setBurst((execution.getBurst() - 1000))
            else:
                execution.setBurst((execution.getBurst() - 1000))
            execution.setBurst() #update the remaining time to complete
            execution.setNumberExecution() #update the number of times this process has executed in a row
            if execution.getNumberExecution() == 2:
                #use the update function that has yet to be implemented
                #it would look like execution.setPriority(updates())
                execution.setNumberExecution(0)
            queue2.put(execution)
        else:
            execution = queue2.get()
            #find algorithm to run it for one clock cycle according to their time slot
            execution.setBurst() #update the remaining time to complete 
            execution.setNumberExecution() #update the number of times this process has executed in a row
            if execution.getNumberExecution() == 2:
                #use the update function that has yet to be implemented
                #it would look like execution.setPriority(updates())
                execution.setNumberExecution(0)
            queue1.put(execution)


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