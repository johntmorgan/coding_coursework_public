#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:52:30 2023

@author: johnmorgan
"""

import asyncio
from asyncio import Future


async def bar(future):
    print("bar will sleep for 3 seconds")
    await asyncio.sleep(3)
    print("bar resolving the future")
    future.done()
    future.set_result("future is resolved")


async def foo(future):
    print("foo will await the future")
    await future
    print("foo finds the future resolved")


async def main():
    future = Future()
    results = await asyncio.gather(foo(future), bar(future))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("main exiting")

    # syntax for Python 3.7
    # asyncio.run(main())
    # print("main exiting")
