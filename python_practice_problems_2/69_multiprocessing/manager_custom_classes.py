#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:39:52 2023

@author: johnmorgan
"""

from multiprocessing.managers import BaseManager
from multiprocessing import Process
import time

# port number on which the manager runs and another can
# connect at
port_num = 55555


class Utility:
    def capitalize(self, name):
        return name.capitalize()


class MyManager(BaseManager):
    pass


MyManager.register('UtilityClass', Utility)


def process_task():
    my_manager = MyManager(address=('127.0.0.1', port_num))
    my_manager.register('UtilityClass')
    my_manager.connect()

    utility = my_manager.UtilityClass()
    print(utility.capitalize("hello"))


if __name__ == '__main__':
    my_manager = MyManager(address=('127.0.0.1', port_num))

    my_manager.start()
    Process(target=process_task).start()

    time.sleep(3)
    print("Main process exiting")