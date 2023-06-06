#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:52:47 2023

@author: johnmorgan
"""

from concurrent.futures import ThreadPoolExecutor
import time

def square(item):
    # simulate a computation by sleeping
    time.sleep(5)
    return item * item

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    future = executor.submit(square, 7)

    print("is running : " + str(future.running()))
    print("is done : " + str(future.done()))
    print("Attempt to cancel : " + str(future.cancel()))
    print("is cancelled : " + str(future.cancelled()))

    executor.shutdown()
