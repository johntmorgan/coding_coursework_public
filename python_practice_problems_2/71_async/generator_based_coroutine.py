#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:48:39 2023

@author: johnmorgan
"""

import asyncio

@asyncio.coroutine
def go_to_sleep(sleep):
    print("sleeping for " + str(sleep) + " seconds")
    yield from asyncio.sleep(sleep)


@asyncio.coroutine
def do_something_important(sleep):
    # what is more important than getting
    # enough sleep!
    yield from go_to_sleep(sleep)
