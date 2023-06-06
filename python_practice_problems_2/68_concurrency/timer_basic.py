#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:29:19 2023

@author: johnmorgan
"""

from threading import Timer
from threading import current_thread
import time


def say_hi(name):
    print("{0} says Hi {1}!".format(current_thread().getName(), name))


timer = Timer(1, say_hi, args=["reader"])
timer.start()

# time.sleep(2)

print("{0} exiting".format(current_thread().getName()))
