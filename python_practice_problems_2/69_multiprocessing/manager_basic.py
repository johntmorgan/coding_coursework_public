#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:32:09 2023

@author: johnmorgan
"""

from multiprocessing.managers import BaseManager, ListProxy
from multiprocessing import Process, Manager
from multiprocessing import current_process
from threading import Thread
import time, multiprocessing, random


def ProcessA(port_num):
    my_string = "hello World"
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string', callable=lambda: my_string)
    server = manager.get_server()

    Thread(target=shutdown,args=(server,)).start()

    server.serve_forever()


def ProcessB(port_num):
    manager = BaseManager(address=('127.0.0.1', port_num))
    manager.register('get_my_string')
    manager.connect()
    proxy_my_string = manager.get_my_string()

    print("In ProcessB repr(proxy_my_string) = {0}".format(repr(proxy_my_string)))
    print("In ProcessB str(proxy_my_string) = {0}".format(str(proxy_my_string)))

    print(proxy_my_string)
    print(proxy_my_string.capitalize())
    print(proxy_my_string._callmethod("capitalize"))


def shutdown(server):
    time.sleep(3)
    server.stop_event.set()



if __name__ == '__main__':
    port_num = random.randint(10000, 60000)

    # Start another process which will access the shared string
    p1 = Process(target=ProcessA, args=(port_num,), name="ProcessA")
    p1.start()

    time.sleep(1)

    p2 = Process(target=ProcessB, args=(port_num,), name="ProcessB")
    p2.start()

    p1.join()
    p2.join()