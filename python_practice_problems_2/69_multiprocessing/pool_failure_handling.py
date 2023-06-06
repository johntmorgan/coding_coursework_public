#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:57:34 2023

@author: johnmorgan
"""

from multiprocessing import Pool, Queue
import os
import random

random.seed()


def square(arg):
    i = random.randrange(0, 5)
    tmp = arg
    if i % 5 is 0:
        print("injecting failure", flush=True)
        tmp = None
    try:
        res = None
        res = tmp * tmp
    except:
        square.q.put(arg)

    return res


def init(main_id, q):
    print("pool process with id {0} received a task from main process with id {1}".
          format(os.getpid(), main_id),
          flush=True)
    square.q = q


def queue_to_list(q):
    i = 0
    lst = list()
    while not q.empty():
        lst.append(q.get())
        i += 1

    return lst, i


if __name__ == '__main__':
    q = Queue()
    failures = 0
    done = False
    lst = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    pool = Pool(processes=5, initializer=init,
                initargs=(os.getpid(), q),
                maxtasksperchild=50)

    final_results = list()
    while not done:
        res = pool.map(square, lst, chunksize=2)
        # print(res)
        final_results.append(res)

        if not q.empty():
            lst, i = queue_to_list(q)
            failures += i
        else:
            done = True

    print("failures: " + str(failures))
    print("final resultfinal_results", final_results)