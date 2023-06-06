#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:09:46 2023

@author: johnmorgan
"""

from multiprocessing.managers import BaseManager, BaseProxy
from multiprocessing import Process
import time

port_num = 55555


def process_task():
    manager = BaseManager(address=('', port_num))
    manager.register('get_pair')
    manager.connect()

    obj1 = manager.get_pair(1,3)
    obj2 = manager.get_pair(2,4)

    # verify two different objects are created
    print(obj1.get_x())
    print(obj2.get_x())


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

if __name__ == '__main__':
    p1 = Process(target=process_task)
    manager = BaseManager(address=('', port_num))

    manager.register('get_pair', Pair)

    manager.start()
    p1.start()
    time.sleep(3)
    manager.shutdown()
