#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:32:58 2023

@author: johnmorgan
"""

import asyncio

# Note @types.coroutine would NOT work here

@asyncio.coroutine
def coro3(k):
    return k + 3

# Do not need to decorate the other functions
# Already using yield from, therefore generator-based coroutines
# Program still ok if decorated though

def coro2(j):
    j = j * j
    result = yield from coro3(j)
    return result

def coro1():
    i = 0
    while i < 100:
        final_result = yield from coro2(i)
        print("f({0}) = {1}".format(i, final_result))
        i += 1


if __name__ == "__main__":

    # The first 100 natural numbers evaluated for the following expression
    # x^2 + 3

    cr = coro1()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cr)