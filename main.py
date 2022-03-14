from hashlib import new
from Process import Process

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
        arr_time = x[1]
        burst = x[2]
        priority = x[3]
        process = Process(pid,arr_time,burst,priority)
        a.append(process)
        count = count + 1
        if count == 3:
            break
    return a


queue1 = []
queue2 = []
pass1 = read_file()
print(str(create_processes(pass1, queue1)))
print(queue1)