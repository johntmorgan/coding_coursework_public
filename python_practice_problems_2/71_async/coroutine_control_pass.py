#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:50:32 2023

@author: johnmorgan
"""

from threading import current_thread
import asyncio
import time

@asyncio.coroutine
def go_to_sleep(sleep):
    print("sleeping for " + str(sleep) + " seconds in thread " + current_thread().getName())
    yield from asyncio.sleep(sleep)


@asyncio.coroutine
def do_something_important(sleep):
    yield from go_to_sleep(sleep)


if __name__ == "__main__":
    now = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(do_something_important(1), do_something_important(2), do_something_important(3)))
    end = time.time()
    print("total time to run the script : " + str(end - now))
    loop.close()