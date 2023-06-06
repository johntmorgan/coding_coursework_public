#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:46:10 2023

@author: johnmorgan
"""

def single_non_duplicate(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if mid % 2 != 0:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]
    
    
nums = [1,1,2,2,3,3,4,4,5,8,8]
print(single_non_duplicate(nums))