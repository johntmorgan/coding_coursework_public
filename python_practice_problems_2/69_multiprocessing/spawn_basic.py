#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:34:06 2023

@author: johnmorgan
"""

from multiprocessing import Process
import multiprocessing
import educative

def process_task():
    print("I am child process")


if __name__ == '__main__':

    # Change the method to 'spawn' and verify 
    # that the modules are reimported in the child
    # process
    multiprocessing.set_start_method('spawn')
    process = Process(target=process_task)
    process.start()
    process.join()
    print("I am parent process")
