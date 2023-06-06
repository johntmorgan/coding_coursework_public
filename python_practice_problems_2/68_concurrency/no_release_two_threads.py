#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:23:09 2023

@author: johnmorgan
"""

# Hangs

from threading import Condition
from threading import Thread
from threading import Lock
from threading import current_thread
import time

flag = False

lock = Lock()
cond_var = Condition(lock)


def child_task():
    global flag
    name = current_thread().getName()

    cond_var.acquire()
    while not flag:
        cond_var.wait()
        print("\n{0} woken up \n".format(name), flush=True)

    print("\n{0} exiting\n".format(name), flush=True)


if __name__ == "__main__":
    thread1 = Thread(target=child_task, name="thread1")
    thread1.start()

    thread2 = Thread(target=child_task, name="thread2")
    thread2.start()

    time.sleep(1)

    cond_var.acquire()
    flag = True
    cond_var.notify_all()
    cond_var.release()

    print("main thread exits", flush=True)