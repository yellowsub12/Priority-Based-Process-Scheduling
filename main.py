from Process import Process

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
    print(array)
    count = 1
    for i in array:
        temp = array[count]
        x = temp.split()
        pid = x[0]
        arr_time = x[1]
        burst = x[2]
        priority = x[3]
        process = Process(pid,arr_time,burst,priority)
        count = count + 1
    return process


queue1 = []
queue2 = []
pass1 = read_file()
queue1.append(create_processes(pass1))
print(queue1)