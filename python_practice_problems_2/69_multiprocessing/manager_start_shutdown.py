#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:33:58 2023

@author: johnmorgan
"""

from multiprocessing.managers import BaseManager
from multiprocessing import Process
import time

# port number on which the manager runs and another can
# connect at
port_num = 55555


def process_task():
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string')
    manager.connect()
    proxy = manager.get_my_string()

    print(repr(proxy))
    print(str(proxy))

    print(proxy.isdigit())
    print(proxy.capitalize())


if __name__ == '__main__':
    manager = BaseManager(address=('127.0.0.1', port_num))

    # Register our type
    my_string = "educative"
    manager.register('get_my_string', callable=lambda: my_string)
    manager.start()

    p = Process(target=process_task)
    p.start()

    time.sleep(3)
    print("Exiting main process")
    manager.shutdown()
