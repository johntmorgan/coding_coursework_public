#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:52:58 2023

@author: johnmorgan
"""

import inspect

var = None


def nested_generator():
    for _ in range(5):
        k = yield
        print("inner generator received = " + str(k))


def outer_generator():
    global var
    nested_gen = nested_generator()
    var = nested_gen
    yield from nested_gen


if __name__ == "__main__":

    gen = outer_generator()
    next(gen)

    try:
        gen.close()
        print("Outer generator state: " + inspect.getgeneratorstate(gen))
        print("Inner generator state: " + inspect.getgeneratorstate(var))

    except StopIteration:
        pass