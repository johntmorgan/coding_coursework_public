#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:02:24 2023

@author: johnmorgan
"""

from threading import Thread
from threading import Lock
from threading import Barrier
from threading import Semaphore
from threading import current_thread
import random

class UberSeating():
    def __init__(self):
        self.dem_count = 0
        self.rep_count = 0
        self.lock = Lock()
        self.barrier = Barrier(4)
        self.dems_waiting = Semaphore(0)
        self.reps_waiting = Semaphore(0)
        self.ride_count = 0
        
    def drive(self):
        self.ride_count += 1
        print("Uber ride #{0} filled and leaving".format(self.ride_count))
        
    def seated(self, party):
        print("\n{0} {1} seated".format(party, current_thread().getName()))
        
    def seat_democrat(self):
        ride_leader = False
        self.lock.acquire()
        self.dem_count += 1
        
        if self.dem_count == 4:
            self.dems_waiting.release()
            self.dems_waiting.release()
            self.dems_waiting.release()
            ride_leader = True
            self.dem_count -= 1
        elif self.dem_count == 2 and self.rep_count >= 2:
            self.dems_waiting.release()
            self.reps_waiting.release()
            self.reps_waiting.release()
            ride_leader = True
            self.dem_count -= 2
            self.rep_count -= 2
        else:
            self.lock.release()
            self.dems_waiting.acquire()
            
        self.seated("Democrat")
        self.barrier.wait()
        
        if ride_leader is True:
            self.drive()
            self.lock.release()
    
    def seat_republican(self):
        ride_leader = False
        self.lock.acquire()
        self.rep_count += 1
        
        if self.rep_count == 4:
            self.reps_waiting.release()
            self.reps_waiting.release()
            self.reps_waiting.release()
            ride_leader = True
            self.rep_count -= 1
        elif self.rep_count == 2 and self.dem_count >= 2:
            self.reps_waiting.release()
            self.dems_waiting.release()
            self.dems_waiting.release()
            ride_leader = True
            self.rep_count -= 2
            self.dem_count -= 2
        else:
            self.lock.release()
            self.reps_waiting.acquire()
            
        self.seated("Republican")
        self.barrier.wait()
        
        if ride_leader is True:
            self.drive()
            self.lock.release()

# May hang if uneven numbers called
# So used controlled simulation instead

def random_simulation():
    problem = UberSeating()
    dems = 0
    reps = 0
    
    riders = list()
    for _ in range(16):
        toss = random.randint(0, 1)
        if toss == 1:
            riders.append(Thread(target=problem.seat_democrat))
            dems += 1
        else:
            riders.append(Thread(target=problem.seat_republican))
            reps += 1
    print("Total {0} dems and {1} reps".format(dems, reps), flush=True)
    for rider in riders:
        rider.start()
        
    for rider in riders:
        rider.join()
        
        
def controlled_simulation():
    problem = UberSeating()
    dems = 10
    reps = 10
    total = 20

    print("Total {0} dems and {1} reps".format(dems, reps), flush=True)
    
    riders = list()
    while total is not 0:
        toss = random.randint(0, 1)
        if toss == 1 and dems is not 0:
            riders.append(Thread(target=problem.seat_democrat))
            dems -= 1
        elif toss == 0 and reps is not 0:
            riders.append(Thread(target=problem.seat_republican))
            reps -= 1

    for rider in riders:
        rider.start()
        
    for rider in riders:
        rider.join()

if __name__ == "__main__":
    controlled_simulation()