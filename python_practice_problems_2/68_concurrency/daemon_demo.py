#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:09:22 2023

@author: johnmorgan
"""

from threading import Thread
from threading import current_thread
import time


def regular_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)

regularThread = Thread(target=regular_thread_task, name="regularThread", daemon=False)
regularThread.start()  # start the regular thread

time.sleep(3)

print("Main thread exiting but Python program doesn't")

from threading import Thread
from threading import current_thread
import time

def daemon_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)

regularThread = Thread(target=daemon_thread_task, name="daemonThread", daemon=True)
regularThread.start()  # start the daemon thread

time.sleep(3)

print("Main thread exiting and Python program too")