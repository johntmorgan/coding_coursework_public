#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:44:36 2023

@author: johnmorgan
"""

from threading import Condition
from threading import Thread
from threading import current_thread
import time

class Barrier(object):
    def __init__(self, size):
        self.barrier_size = size
        self.thread_count = 0
        self.released_count = self.barrier_size
        self.cond = Condition()
        
    def arrived(self):
        self.cond.acquire()
        # Do not let thread re-hit barrier until others released
        while self.reached_count == self.barrier_size:
            self.cond.wait()
        
        self.reached_count += 1
        if self.reached_count == self.barrier_size:
            self.released_count = self.barrier_size
        else:
            # Place in while loop in case thread wakes up spuriously
            # Track released count so no awoken thread gets stuck here
            while self.reached_count < self.barrier_size:
                self.cond.wait()
        self.released_count -= 1
        if self.released_count == 0:
            self.reached_count = 0
        self.cond.notifyAll()
        self.cond.release()

def thread_process(sleep_for):
    time.sleep(sleep_for)
    print("Thread {0} reached the barrier".format(current_thread().getName()))
    barrier.arrived()

    time.sleep(sleep_for)
    print("Thread {0} reached the barrier".format(current_thread().getName()))
    barrier.arrived()

    time.sleep(sleep_for)
    print("Thread {0} reached the barrier".format(current_thread().getName()))
    barrier.arrived()


if __name__ == "__main__":
    barrier = Barrier(3)

    t1 = Thread(target=thread_process, args=(0,))
    t2 = Thread(target=thread_process, args=(0.5,))
    t3 = Thread(target=thread_process, args=(1.5,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()