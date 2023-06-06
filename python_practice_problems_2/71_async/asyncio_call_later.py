#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:26:48 2023

@author: johnmorgan
"""

import asyncio, random, time
from threading import Thread
from threading import current_thread
from asyncio import Future

def resolver(future):
    print("Is loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))

    time.sleep(2)
    future.set_result(None)


async def coro():
    future = Future()

    loop = asyncio.get_event_loop()
    loop.call_later(5, resolver, future)

    print("Is loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))


    await future
    print("coro exiting")


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    print("Is loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))

    loop.run_until_complete(coro())
    print("main exiting")
