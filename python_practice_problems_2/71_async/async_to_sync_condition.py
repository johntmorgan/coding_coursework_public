#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:14:09 2023

@author: johnmorgan
"""

from threading import Thread
from threading import Condition
from threading import current_thread
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
        self.cond = Condition()
        self.is_done = False

    def work(self, callback):
        super().work(callback)
        print("{0} thread notifying".format(current_thread().getName()))
        self.cond.acquire()
        self.cond.notifyAll()
        self.is_done = True
        self.cond.release()
        
    def execute(self, callback):
        super().execute(callback)
        self.cond.acquire()
        while self.is_done is False:
            self.cond.wait()
        print("{0} thread woken up".format(current_thread().getName()))
        self.cond.release()

def say_hi():
    print("Hi")


if __name__ == "__main__":
    aexec = SyncExecutor()
    aexec.execute(say_hi)

    print("main thread exiting")