#!/usr/bin/python
import time

def stopwatch(seconds):
    start = time.time()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print("loop cycle time: %f, seconds count: %02d") % (time.time() , elapsed) 
        time.sleep(1)  

stopwatch(20)