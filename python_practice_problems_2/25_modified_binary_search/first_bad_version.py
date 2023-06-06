#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:35:55 2023

@author: johnmorgan
"""

from api import *

version_api = api(0)

def is_bad_version(v):
    return version_api.is_bad(v)

def first_bad_version(n):
# -- DO NOT CHANGE THIS SECTION
    version_api.n = n
# -- 

    low = 1
    high = n
    counter = 0
    while low < high:
        mid = (high + low) // 2
        if not is_bad_version(mid):
            low = mid + 1
        else:
            high = mid
        counter += 1
    if is_bad_version(low):
        return low, counter
    return mid, counter