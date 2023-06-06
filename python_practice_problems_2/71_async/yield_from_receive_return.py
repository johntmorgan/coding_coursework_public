#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:34:42 2023

@author: johnmorgan
"""

def nested_generator():
    i = 0
    while i < 5:
        i += 1
        yield i

    return 999


def outer_generator():
    nested_gen = nested_generator()
    ret_val = yield from nested_gen
    print("received in outer generator: " + str(ret_val))


if __name__ == "__main__":

    gen = outer_generator()

    for item in gen:
        print(item)
