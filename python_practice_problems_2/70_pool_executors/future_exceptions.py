#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:54:20 2023

@author: johnmorgan
"""

from concurrent.futures import ThreadPoolExecutor


def square(item):
    item = None
    return item * item


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=1)
    lst = list()

    future = executor.submit(square, 7)
    ex = future.exception()
    print(ex)

    executor.shutdown()
