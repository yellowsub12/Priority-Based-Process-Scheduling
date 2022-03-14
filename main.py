from hashlib import new
from multiprocessing.connection import wait
from Process import Process
import queue
import time

global flag1, flag2
flag1 = False #queue1 flag
flag2 = True #queue2 flag
global clock
clock = 0

def read_file():
    open_file = open("input.txt", "r")
    lines = []
    for line in open_file:
        lines.append(line)
    open_file.close()
    return lines

def create_processes(array, a):
    global nb_processes 
    nb_processes = array[0]
    new_array = array[1:]
    count = 0
    for i in new_array:
        i = new_array[count]
        x = i.split()
        pid = x[0]
        arr_time = int(x[1]) / 1000
        burst = int(x[2]) / 1000
        priority = x[3]
        process = Process(pid,arr_time,burst,priority)
        a.put(process)
        count = count + 1
        if count == len(new_array):
            break

#def updates():
#    waiting_time = sum_of_waiting_times
#    bonus = 10*waiting_time/(clock - arrival_time)
#    new_priority = max(100,min(old_priority - bonus + 5139))

def main():
    start_time = time.time()
    queue1 = queue.Queue()
    queue2 = queue.Queue()
    pass1 = read_file()
    create_processes(pass1, queue1)
    while True:
        if queue1.empty():
            flag1 = False
        else:
            flag2 = False
        if flag1 == True:
            process_start = time.time()
            x = queue1.get()
            #updates()
            queue2.put()
            flag1 = False
            flag2 = True
            exec_time = time.time()
            print("Process " + x + "has executed in " + (process_start - exec_time))
        elif flag2 == True:
            process_start = time.time()
            x = queue2.get()
            #updates()
            queue1.put()
            exec_time = time.time()
            flag1 = True
            flag2 = False
            exec_time = time.time()
            print("Process " + x + "has executed in " + (process_start - exec_time))
        clock = clock + 1
        break #loop only executes once, alternative needs to be found.
    end_time = time.time()
    print(end_time - start_time)

if __name__ == "__main__":
    main()