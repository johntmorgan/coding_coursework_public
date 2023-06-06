#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:33:03 2023

@author: johnmorgan
"""

# Basic

# from threading import Barrier
# from threading import Thread
# import random
# import time


# def thread_task():
#     time.sleep(random.randint(0, 7))
#     print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
#     barrier.wait()
#     print("\nThreads released")


# num_threads = 5
# barrier = Barrier(num_threads)
# threads = [0] * num_threads

# for i in range(num_threads):
#     threads[i - 1] = Thread(target=thread_task)

# for i in range(num_threads):
#     threads[i].start()


# Action

# from threading import Barrier
# from threading import Thread
# from threading import current_thread
# import random
# import time


# def thread_task():
#     time.sleep(random.randint(0, 5))
#     print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
#     barrier.wait()


# def when_all_threads_released():
#     print("All threads released, reported by {0}".format(current_thread().getName()))

# num_threads = 5
# barrier = Barrier(num_threads, action=when_all_threads_released)
# threads = [0] * num_threads

# for i in range(num_threads):
#     threads[i - 1] = Thread(target=thread_task)

# for i in range(num_threads):
#     threads[i].start()


# Abort

from threading import Barrier
from threading import Thread
import time


def thread_task():
    print("\nCurrently {0} threads blocked on barrier".format(barrier.n_waiting))
    barrier.wait()
    print("Barrier broken")


num_threads = 5
barrier = Barrier(num_threads + 1)
threads = [0] * num_threads

for i in range(num_threads):
    threads[i - 1] = Thread(target=thread_task)

for i in range(num_threads):
    threads[i].start()

time.sleep(3)

print("Main thread about to invoke abort on barrier")
barrier.abort()
