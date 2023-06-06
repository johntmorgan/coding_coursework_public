#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:53:53 2023

@author: johnmorgan
"""

from threading import Thread
from threading import Semaphore
import time

def printer_thread():
    global primeHolder

    while not exitProg:
        # wait for a prime number to become available
        sem_find.acquire()

        # print the prime number
        print(primeHolder)
        primeHolder = None

        # let the finder thread find the next prime
        sem_print.release()

def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True

def finder_thread():
    global primeHolder

    i = 1

    while not exitProg:

        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)

        primeHolder = i

        # let the printer thread know we have
        # a prime available for printing
        sem_find.release()

        # wait for printer thread to complete
        # printing the prime number
        sem_print.acquire()

        i += 1

sem_find = Semaphore(0)
sem_print = Semaphore(0)
primeHolder = None
exitProg = False

printerThread = Thread(target=printer_thread)
printerThread.start()

finderThread = Thread(target=finder_thread)
finderThread.start()

# Let the threads run for 3 seconds
time.sleep(3)

exitProg = True

printerThread.join()
finderThread.join()