#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:54:28 2023

@author: johnmorgan
"""

def find_min(nums):
    low, high = 0, len(nums) - 1
    mid = None
    while low <= high:
        mid = (low + high) // 2
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[high] < nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return min(nums[mid], nums[mid + 1])

nums = [5,7,17,21,22,2,4]
print(find_min(nums))