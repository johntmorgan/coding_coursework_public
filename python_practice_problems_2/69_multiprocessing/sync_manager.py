#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:22:53 2023

@author: johnmorgan
"""

from multiprocessing.managers import SyncManager
from multiprocessing import Process
import time

# port number on which the manager runs and another can
# connect at
port_num = 55555


def process_task(sem):
    manager = SyncManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string')
    manager.connect()
    proxy = manager.get_my_string()

    print(repr(proxy))
    print(str(proxy))
    print("child process exiting in 5 seconds")

    time.sleep(5)
    sem._callmethod('release')

    # invoking methods on the proxy's referent
    print(proxy._callmethod('isdigit'))
    print(proxy._callmethod('capitalize'))


if __name__ == '__main__':
    manager = SyncManager(address=('127.0.0.1', port_num))

    # Register our type
    my_string = "educative"
    manager.register('get_my_string', callable=lambda: my_string)
    manager.start()

    # get a proxy for a Semaphore
    sem = manager.Semaphore(0)

    # pass the semahore to the other process
    p = Process(target=process_task, args=(sem,))
    p.start()

    # wait for the semaphore to be set
    sem._callmethod('acquire')

    print("Main process exiting")
