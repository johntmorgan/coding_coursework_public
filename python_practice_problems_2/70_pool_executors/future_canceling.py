#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:55:02 2023

@author: johnmorgan
"""

from concurrent.futures import ThreadPoolExecutor
import time


def square(item):
    time.sleep(5)
    print(item * item)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)

    future1 = executor.submit(square, 7)
    future2 = executor.submit(square, 9)

    print("Attempt to cancel : " + str(future2.cancel()))
    print("is running : " + str(future2.running()))
    print("is done : " + str(future2.done()))
    print("is cancelled : " + str(future2.cancelled()))

    executor.shutdown()