#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:23:07 2023

@author: johnmorgan
"""

import asyncio
import time

async def do_something_important():
    await asyncio.sleep(10)

if __name__ == "__main__":
  start = time.time()

  # Python 3.7+ syntax
  # asyncio.run(do_something_important())

  # Python 3.5 syntax
  loop = asyncio.get_event_loop()
  loop.run_until_complete(do_something_important())

  print("Program ran for {0} seconds".format(time.time() - start))