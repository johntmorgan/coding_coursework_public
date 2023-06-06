#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:00:32 2023

@author: johnmorgan
"""

def find_missing_number(nums):
    for i in range(len(nums)):
        while nums[i] != i and nums[i] < len(nums):
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)
    
    
nums = [0,1,2,4]
print(find_missing_number(nums))

nums = [3,0,1,4]
print(find_missing_number(nums))