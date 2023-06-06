#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:27:15 2023

@author: johnmorgan
"""

from multiprocessing import Barrier, Process, current_process
import random
import time


def process_task():
    time.sleep(random.randint(0, 5))
    print("\nCurrently {0} processes blocked on barrier".format(barrier.n_waiting), flush=True)
    barrier.wait()


def when_all_processes_released():
    print("\nAll processes released, reported by {0}".format(current_process().name), flush=True)


num_processes = 5
barrier = Barrier(num_processes, action=when_all_processes_released)
processes = [0] * num_processes

for i in range(num_processes):
    processes[i - 1] = Process(target=process_task)

for i in range(num_processes):
    processes[i].start()