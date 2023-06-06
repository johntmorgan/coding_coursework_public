#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:56:45 2023

@author: johnmorgan
"""

def find_tribonacci(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    trib_array = [0, 1, 1] + [-float('inf')] * (n - 2)
    for i in range(3, len(trib_array)):
        trib_array[i] = trib_array[i - 1] + trib_array[i - 2] + trib_array[i - 3]
    return trib_array[n]

# Or don't even use an array

def find_tribonacci(n):
    if n < 3:
        return 0 if n == 0 else 1
    first, second, third = 0, 1, 1
    for _ in range(n - 2):
        first, second, third = second, third, first + second + third
    return third
    
    
print(find_tribonacci(10))
print(find_tribonacci(15))