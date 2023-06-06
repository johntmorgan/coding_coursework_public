#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:07:21 2023

@author: johnmorgan
"""

# Bugged
# get() is blocking
# Both processes may see not empty at the same time, one gets blocked

from multiprocessing import Process, Queue, current_process
import multiprocessing, sys
import random


def child_process(q):
    count = 0
    while not q.empty():
        print(q.get())
        count += 1

    print("child process {0} processed {1} items from the queue".format(
        current_process().name, count), flush=True)

if __name__ == '__main__':
    multiprocessing.set_start_method("forkserver")
    q = Queue()
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    
    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q,))
    p2 = Process(target=child_process, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()