#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:06:03 2023

@author: johnmorgan
"""

from multiprocessing import Process
from multiprocessing import current_process
import os


def process_task(x, y, z, key1, key2):
    print("\n{0} has pid: {1} with parent pid: {2}".format(
        current_process().name, os.getpid(), os.getppid()))
    print("Received arguemnts {0} {1} {2} {3} {4}\n".format(
        x, y, z, key1, key2))


process = Process(target=process_task,
                  name="process-1",
                  args=(1, 2, 3),
                  kwargs={
                      'key1': 'arg1',
                      'key2': 'arg2'
                  })
process.start()
process.join()