#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:35:55 2023

@author: johnmorgan
"""

import asyncio
import types
from collections.abc import Iterable, Generator

# hello_routine isn't a traditional generator that
# returns items in a sequence
@asyncio.coroutine
def hello_routine():
    print("hello world")


# coro becomes a generator based coroutine itself on
# account of using the yield from expression
def coro():
    yield from hello_routine()


if __name__ == "__main__":
    gen = coro()

    # hello_routine is an iterable, generator and a
    # generator based coroutine
    print(isinstance(hello_routine(), types.GeneratorType))
    print(isinstance(hello_routine(), Iterable))
    print(isinstance(hello_routine(), Generator))

    # in fact, coro which yields from hello_routine is also
    # an iterable and a generator based coroutine
    print(isinstance(gen, types.GeneratorType))
    print(isinstance(gen, Iterable))
    print(isinstance(gen, Generator))

    for _ in gen:
        pass
