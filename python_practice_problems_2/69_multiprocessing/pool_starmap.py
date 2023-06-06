#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:55:06 2023

@author: johnmorgan
"""

from multiprocessing import Pool
import time
import os


def square(arg1, arg2):
    return arg2 + '-' + str(arg1 * arg1)


def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".
          format(os.getpid(), main_id), flush=True)


def on_success(new_result):
    for x in new_result:
        print("\n" + x)


def on_error(err):
    print("Error : " + str(err))


if __name__ == '__main__':
    pool = Pool(processes=5, initializer=init,
                initargs=(os.getpid(),),
                maxtasksperchild=50)

    res = pool.starmap_async(square,
                             ((1, 'chunk1'),
                              (3, 'chunk2'),
                              (5, 'chunk3'),
                              (7, 'chunk4'),
                              (9, 'chunk5')),
                             chunksize=2,
                             callback=on_success,
                             error_callback=on_error)

    pool.close()
    pool.join()