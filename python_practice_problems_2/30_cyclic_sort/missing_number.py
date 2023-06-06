#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:43:20 2023

@author: johnmorgan
"""

# Naive
# Quicksort + traverse
# O(nlogn + n)

# Cyclic sort
# O(n)
# O(1) space

from traversal import *

def find_missing_number(nums):
    for i in range(len(nums)):
        while nums[i] != i and nums[i] < len(nums):
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i:
            return i

nums = [0,1,2,4]
print(find_missing_number(nums))

nums = [3,0,1,4]
print(find_missing_number(nums))

nums =[1, 4, 5, 6, 8, 2, 0, 7]
print(find_missing_number(nums))