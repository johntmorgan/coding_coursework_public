#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:09:20 2023

@author: johnmorgan
"""

def min_sub_array_len(target, nums):
    min_len, found = float('inf'), False
    curr_sum = 0
    start, end = 0, 0
    while end < len(nums):
        curr_sum += nums[end]
        if curr_sum >= target:
            while curr_sum - nums[start] >= target:
                curr_sum -= nums[start]
                start += 1
            length = end - start + 1
            if length < min_len:
                min_len = length
                found = True
        end += 1
    if not found:
        return 0
    return min_len

target = 7
nums = [2,3,1,2,4,3]
print(min_sub_array_len(target, nums))