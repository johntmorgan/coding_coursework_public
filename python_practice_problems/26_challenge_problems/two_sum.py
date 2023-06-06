#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:34:13 2023

@author: johnmorgan
"""

def two_sum(arr, t):
    d = {}
    for i, num in enumerate(arr):
        if t - num in d:
            return [d[t - num], i]
        else:
            d[num] = i
    return False