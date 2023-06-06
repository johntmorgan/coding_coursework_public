#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:16:59 2023

@author: johnmorgan
"""

from concurrent.futures import wait
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def square(item):
    if item != 1:
        time.sleep(4)

    return item * item


if __name__ == '__main__':
    lst = list()
    threadExecutor = ThreadPoolExecutor(max_workers=10)
    processExecutor = ProcessPoolExecutor(max_workers=10)

    for i in range(1, 6):
        lst.append(threadExecutor.submit(square, i))

    for i in range(6, 11):
        lst.append(processExecutor.submit(square, i))

    result = wait(lst, timeout=0.01, return_when='FIRST_COMPLETED')
    print("completed futures count: " + str(len(result.done)) + " and uncompleted futures count: " +
          str(len(result.not_done)) + "\n")         

    threadExecutor.shutdown()
    processExecutor.shutdown()