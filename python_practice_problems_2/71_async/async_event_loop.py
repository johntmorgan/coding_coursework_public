#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:31:44 2023

@author: johnmorgan
"""

import asyncio, random, time
from threading import Thread
from threading import current_thread
from asyncio import Future
shutdown = False

async def resolver(future):
    print("Is loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))

    # If just time.sleep, monitor_coro stops printing because loop hogged
    await asyncio.sleep(10)
    future.set_result(None)


async def monitor_coro():
    global shutdown
    
    while shutdown == False:
        print("Alive at {0}".format(time.time()))
        await asyncio.sleep(1)

async def coro():
    global shutdown

    print("coro running")
    future = Future()

    loop = asyncio.get_event_loop()
    monitor_coro_future = asyncio.ensure_future(monitor_coro())
    resolver_future = asyncio.ensure_future(resolver(future))

    print("Is loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))


    await future
    await asyncio.sleep(2)
    shutdown = True

    await monitor_coro_future, resolver_future


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    print("Is loop running in thread {0} = {1}\n".format(current_thread().getName(),
                                                         asyncio.get_event_loop().is_running()))

    loop.run_until_complete(coro())
    print("main exiting")