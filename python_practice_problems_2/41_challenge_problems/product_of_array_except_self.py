#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:02:42 2023

@author: johnmorgan
"""

# Brute force O(n^2)

def product(arr):
    res = [1] * len(arr)
    for index, num in enumerate(arr):
        for res_index in range(len(res)):
            if index != res_index:
                res[res_index] *= num
    return res

# Two pointers, prefix * suffix, sweep both across array at same time
# Suffix covers index = 0, prefix covers len(arr) - 1
# Start prefix at 1, look back, start suffix at end, look forwards
# Sweep both across at same time for O(n)

def product(arr):
    res = [1] * len(arr)
    prefix, suffix = 1, 1
    for i in range(1, len(arr)):
        prefix *= arr[i - 1]
        res[i] *= prefix
        suff_idx = len(arr) - 1 - i
        suffix *= arr[suff_idx + 1]
        res[suff_idx] *= suffix
    return res

arr = [0,-1,2,-3,4,-2]
print(product(arr))