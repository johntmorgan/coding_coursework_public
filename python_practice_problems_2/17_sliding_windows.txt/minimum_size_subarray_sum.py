#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:33:19 2023

@author: johnmorgan
"""

# O(n)
# Space complexity O(1)

def min_sub_array_len(target, nums):
    min_size = float('inf')
    start, length, curr_val = 0, 0, 0
    for index, val in enumerate(nums):
        length += 1
        curr_val += val
        if curr_val >= target:
            while curr_val - nums[start] >= target:
                curr_val = curr_val - nums[start]
                start += 1
                length -= 1
            if length < min_size:
                min_size = length
    if min_size > len(nums):
        return 0
    return min_size

target, nums = 7 , [2,3,1,2,4,3]
print(min_sub_array_len(target, nums))
target, nums = 4 , [1,4,4]
print(min_sub_array_len(target, nums))
target, nums = 11 , [1,1,1,1,1,1,1,1]
print(min_sub_array_len(target, nums))
target, nums = 10 , [1,2,3,4]
print(min_sub_array_len(target, nums))
target, nums = 5 , [1,2,1,3]
print(min_sub_array_len(target, nums))