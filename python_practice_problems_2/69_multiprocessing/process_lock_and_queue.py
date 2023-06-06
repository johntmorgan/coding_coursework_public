#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:47 2023

@author: johnmorgan
"""

from multiprocessing import Process, Queue, current_process, Lock
import multiprocessing, sys
import random
import time

def child_process(q, lock):
    count = 0
    keep_going = True

    while keep_going:
        lock.acquire()
        if not q.empty():
            print(q.get())
            count += 1
        else:
            keep_going = False
        lock.release()
        # Added this sleep so that not all items get processed by
        # a single process
        time.sleep(0.001)

    print("child process {0} processed {1} items from the queue".format(
        current_process().name, count), flush=True)


if __name__ == '__main__':

    multiprocessing.set_start_method("forkserver")
    print("This machine has {0} CPUs".format(str(multiprocessing.cpu_count())))
    lock = Lock()
    q = Queue()

    random.seed()
    for _ in range(100):
        q.put(random.randrange(10))

    p1 = Process(target=child_process, args=(q, lock))
    p2 = Process(target=child_process, args=(q, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
