#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:29:28 2023

@author: johnmorgan
"""

import asyncio
from asyncio import Future

def coro3(k):
    future = Future()
    future.set_result(k+3)
    future.done()
    return future


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