#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:03:11 2023

@author: johnmorgan
"""

from multiprocessing import Process
from multiprocessing import current_process
import os


def process_task():
    print("{0} has pid: {1} with parent pid: {2}".format(current_process().name,
                                                  os.getpid(), os.getppid()))

if __name__ == "__main__":
    process = [0] * 3

    for i in range(0, 3):
        process[i] = Process(target=process_task, name="process-{0}".format(i))
        process[i].start()

    for i in range(0, 3):
        process[i].join()

    print("{0} has pid: {1} ".format(current_process().name, os.getpid()))
    


