#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:52:06 2023

@author: johnmorgan
"""

def nested_generator():
    for _ in range(5):
        try:
            k = yield
            print("inner generator received = " + str(k))
        except Exception:
            print("caught an exception")


def outer_generator():
    nested_gen = nested_generator()
    yield from nested_gen


if __name__ == "__main__":

    gen = outer_generator()
    next(gen)

    for i in range(5):
        try:
            if i == 1:
                gen.throw(Exception("deliberate exception"))
            else:
                gen.send(i)
        except StopIteration:
            pass