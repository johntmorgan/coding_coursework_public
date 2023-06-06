#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:04:31 2023

@author: johnmorgan
"""

from threading import Thread
from threading import Semaphore
import time

# Do not touch

class AsyncExecutor:

    def work(self, callback):
        # simulate asynchronous work
        time.sleep(1)
        # let the invoker take action in a callback
        callback()

    def execute(self, callback):
        Thread(target=self.work, args=(callback,)).start()

# Can touch

class SyncExecutor(AsyncExecutor):
    def __init__(self):
        self.sem = Semaphore(0)        

    def work(self, callback):
        super().work(callback)
        self.sem.release()
        
    def execute(self, callback):
        super().execute(callback)
        self.sem.acquire()

def say_hi():
    print("Hi")


if __name__ == "__main__":
    aexec = SyncExecutor()
    aexec.execute(say_hi)

    print("main thread exiting")