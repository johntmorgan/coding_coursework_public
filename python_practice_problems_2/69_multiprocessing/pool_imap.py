#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:53:48 2023

@author: johnmorgan
"""

from multiprocessing import Pool
import os


def square(arg):
    return arg * arg


def init(main_id):
    print("pool process with id {0} received a task from main process with id {1}".format(os.getpid(), main_id),
          flush=True)

if __name__ == '__main__':
    pool = Pool(processes=5, initializer=init,
                initargs=(os.getpid(),),
                maxtasksperchild=50)

    res = pool.imap_unordered(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                    chunksize=2)

    for sq in res:
        print(sq)