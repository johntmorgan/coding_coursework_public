#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:17:55 2023

@author: johnmorgan
"""

from threading import Condition
from threading import Thread
from threading import current_thread
import time

flag = False

cond_var = Condition()


def child_task():
    global flag
    name = current_thread().getName()

    cond_var.acquire()
    if not flag:
        cond_var.wait()
        print("\n{0} woken up \n".format(name))

    cond_var.release()

    print("\n{0} exiting\n".format(name))


thread1 = Thread(target=child_task, name="thread1")
thread2 = Thread(target=child_task, name="thread2")
thread3 = Thread(target=child_task, name="thread3")

thread1.start()
thread2.start()
thread3.start()

cond_var.acquire()
cond_var.notify_all()
cond_var.release()

thread1.join()
thread2.join()
thread3.join()

print("main thread exits")
