#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:49:23 2022

@author: johnmorgan
"""

def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])
    
print(recursive_sum([1, 3, 6, 7]))

def recursive_count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + recursive_count(arr[1:])
    
print(recursive_count([1, 3, 6, 7]))

def recursive_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], recursive_max(arr[1:]))
    
print(recursive_max([1, 3, 6, 7, 9]))
