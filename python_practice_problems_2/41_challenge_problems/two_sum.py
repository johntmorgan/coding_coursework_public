#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:47:36 2023

@author: johnmorgan
"""

def two_sum(arr, t):
    d = {}
    for index, num in enumerate(arr):
        if t - num in d:
            return [d[t - num], index]
        else:
            d[num] = index
    return []

arr = [2,4,6,8,10,19]
t = 21
print(two_sum(arr, t))