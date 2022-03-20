import threading
import os

interval = 1
clock = 0 
def myPeriodicFunction():
    global clock
    print ("This loops on a timer every %d seconds" % interval)
    clock = clock + 1000
    print("Clock is %d" % clock)
    if clock >= 2000  and clock < 4000 :
        clock = clock + 200
    
def startTimer():
    threading.Timer(interval, startTimer).start()
    myPeriodicFunction()

startTimer()

