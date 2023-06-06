#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:19:12 2023

@author: johnmorgan
"""

from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor
import time


def square(item):
    time.sleep(5 - item)
    return item * item


if __name__ == '__main__':
    lst = list()
    processExecutor = ProcessPoolExecutor(max_workers=10)

    for i in range(1, 6):
        lst.append(processExecutor.submit(square, i))

    result = as_completed(lst, timeout=None)

    for ftr in result:
        print(ftr.result())

    processExecutor.shutdown()
