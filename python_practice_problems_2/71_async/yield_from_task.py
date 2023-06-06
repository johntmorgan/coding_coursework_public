#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:39:47 2023

@author: johnmorgan
"""

import asyncio

def yield_from_task_example():
    # create a task to sleep for 5 seconds
    task = asyncio.get_event_loop().create_task(asyncio.sleep(5))
    yield from task

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(yield_from_task_example())