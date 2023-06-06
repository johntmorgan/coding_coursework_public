#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:27:30 2023

@author: johnmorgan
"""

def coro3(k):
    yield (k + 3)


def coro2(j):
    j = j * j
    yield from coro3(j)


def coro1():
    i = 0
    while True:
        yield from coro2(i)
        i += 1


if __name__ == "__main__":

    # The first 100 natural numbers evaluated for the following expression
    # x^2 + 3

    cr = coro1()
    for v in range(100):
        print("f({0}) = {1}".format(v, next(cr)))