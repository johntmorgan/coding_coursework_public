#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:09:20 2023

@author: johnmorgan
"""

def printer():
    item = None
    while True:
        item = yield
        print(str(item))


if __name__ == "__main__":

    coroutine_object = printer()
    next(coroutine_object)

    print("class name: " + coroutine_object.__class__.__name__)
