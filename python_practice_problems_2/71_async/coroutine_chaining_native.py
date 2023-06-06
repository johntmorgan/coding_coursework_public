#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:34:33 2023

@author: johnmorgan
"""

import asyncio


async def coro3(k):
    return k + 3


async def coro2(j):
    j = j * j
    res = await coro3(j)
    return res


async def coro1():
    i = 0
    while i < 100:
        res = await coro2(i)
        print("f({0}) = {1}".format(i, res))
        i += 1


if __name__ == "__main__":
    # The first 100 natural numbers evaluated for the following expression
    # x^2 + 3
    cr = coro1()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cr)