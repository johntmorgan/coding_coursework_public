#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:15:41 2023

@author: johnmorgan
"""

from threading import Thread
import sys

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        for _ in range(100000):
            self.count += 1


if __name__ == "__main__":
    
    # Sets the thread switch interval
    sys.setswitchinterval(0.005)

    numThreads = 5
    threads = [0] * numThreads
    counter = Counter()

    for i in range(0, numThreads):
        threads[i] = Thread(target=counter.increment)

    for i in range(0, numThreads):
        threads[i].start()

    for i in range(0, numThreads):
        threads[i].join()

    if counter.count != 500000:
        print(" count = {0}".format(counter.count), flush=True)
    else:
        print(" count = 50,000 - Try re-running the program.")