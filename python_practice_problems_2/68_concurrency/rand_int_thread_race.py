#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:33:44 2023

@author: johnmorgan
"""

from threading import *
import random
import time

rand_int = 0


def updater():
    global rand_int
    while 1:
        rand_int = random.randint(1, 9)


def printer():
    global rand_int
    while 1:

        # test
        if rand_int % 5 == 0:
            if rand_int % 5 != 0:
                # and act
                print(rand_int)


if __name__ == "__main__":
    Thread(target=updater, daemon=True).start()
    Thread(target=printer, daemon=True).start()

    # Let the simulation run for 5 seconds
    time.sleep(5)
    
# Fix

from threading import *
import random
import time

rand_int = 0
lock = Lock()

def updater():
    global rand_int
    global lock
    while 1:
        with lock:
          rand_int = random.randint(1, 9)


def printer():
    global rand_int
    global lock
    while 1:

        with lock:
          # test
          if rand_int % 5 == 0:
              if rand_int % 5 != 0:
                  # and act
                  print(rand_int)
