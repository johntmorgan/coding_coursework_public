#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:13:29 2023

@author: johnmorgan
"""

def smallest_missing_positive_integer(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[i] > 0 and nums[i] < len(nums):
            j = nums[i]
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1
    
    
nums = [1,2,3,5]
print(smallest_missing_positive_integer(nums))

nums = [5,3,2,1]
print(smallest_missing_positive_integer(nums))
