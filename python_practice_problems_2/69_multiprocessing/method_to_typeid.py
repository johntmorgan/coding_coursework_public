#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:17:40 2023

@author: johnmorgan
"""

from multiprocessing.managers import BaseManager, BaseProxy
from multiprocessing import Process
import multiprocessing
import time

port_num = 55555


def consumer_process():
    mgr = BaseManager(address=('', port_num))
    mgr.register('ItemWrapper', ItemWrapper)
    mgr.register('get_pair')
    mgr.connect()

    p = mgr.get_pair()
    proxy1 = p.get_item()
    print("proxy1 sees item as : " + str(proxy1.get_wrapped_item()))
    old_val = proxy1.get_wrapped_item()
    proxy1._callmethod('set_wrapped_item', (7,))
    print("proxy1 changes item from {0} to {1}".format(old_val, proxy1.get_wrapped_item()))

    proxy2 = mgr.get_pair().get_item()
    print("proxy2 sees item as : " + str(proxy2.get_wrapped_item()))
    old_val = proxy2.get_wrapped_item()
    proxy2.set_wrapped_item(11)
    print("proxy2 changes item from {0} to {1}".format(old_val, proxy2.get_wrapped_item()))
    print("proxy1 sees item as : " + str(proxy1.get_wrapped_item()))


def producer_process():
    manager = BaseManager(address=('', port_num))

    pair = Pair(15, 6)

    manager.register('ItemWrapper', ItemWrapper)
    manager.register('get_pair', callable=lambda: pair,
                     method_to_typeid={'get_item': 'ItemWrapper'})

    manager.start()
    time.sleep(3)
    print("\nAfter changes in consumer process, the producer process sees item as = {0}".format(pair.get_item().retrieve()))
    manager.shutdown()


class ItemWrapper:
    def __init__(self, res):
        self.item = res

    def set_wrapped_item(self, new_item):
        self.item.change(new_item)

    def get_wrapped_item(self):
        return self.item.retrieve()


class Item:

    def __init__(self):
        self.item = "intialized"

    def change(self, new_item):
        self.item = new_item

    def retrieve(self):
        return self.item;


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.i = Item()

    def get_item(self):
        return self.i

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


if __name__ == '__main__':
    p1 = Process(target=producer_process)
    p2 = Process(target=consumer_process)

    p1.start()
    time.sleep(2)
    p2.start()

    p2.join()
    p1.join()
