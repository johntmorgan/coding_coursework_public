#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:00:44 2023

@author: johnmorgan
"""

from concurrent.futures import ThreadPoolExecutor


def square(item):
    return item * item


def my_special_callback(ftr):
    res = ftr.result()
    print("my_special_callback invoked " + str(res))


def my_other_special_callback(ftr):
    res = ftr.result()
    print("my_other_special_callback invoked " + str(res * res))


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    future = executor.submit(square, 7)
    future.add_done_callback(my_special_callback)
    future.add_done_callback(my_other_special_callback)

    executor.shutdown(wait=False)
