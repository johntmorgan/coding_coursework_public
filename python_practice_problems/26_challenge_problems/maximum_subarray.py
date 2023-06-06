#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:16:30 2023

@author: johnmorgan
"""

def max_sub_array(nums):
    max_sum = -float('inf')
    best_arr = []
    for i, num in enumerate(nums):
        if i == 0:
            best = num
        else:
            best = max(num, num + best_arr[i - 1])
        if best > max_sum:
            max_sum = best
        best_arr.append(best)
    return max_sum
    
    
nums = [-2, 1, 0, 4, -1, 7, 1, 5, -8]
print(max_sub_array(nums))