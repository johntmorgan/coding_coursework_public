#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:23:43 2023

@author: johnmorgan
"""

from threading import Thread
from threading import Event
import time


def task1():
    event.wait()
    event.wait()
    event.wait()
    print("thread invoked wait() thrice")


def task2():
    time.sleep(1)
    event.set()


event = Event()

thread1 = Thread(target=task1)
thread1.start()

thread2 = Thread(target=task2)
thread2.start()

thread1.join()
thread2.join()