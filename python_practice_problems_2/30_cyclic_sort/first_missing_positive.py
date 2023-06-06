#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:43:14 2023

@author: johnmorgan
"""

# Naive: search for each integer in array one at a time, O(n^2)
# Naive 2: sort O(nlogn)
# Naive 3: hash table O(n) but also O(n) space

# O(n) time complexity
# O(1)

def first_missing_positive(nums):
    for i in range(len(nums)):
        while 1 <= nums[i] <= len(nums) and nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    largest = max(nums)
    if largest > 0:
        return largest + 1
    else:
        return 1


nums = [1,2,3,5]
print(first_missing_positive(nums))

nums = [2,3,4,5,6]
print(first_missing_positive(nums))

nums = [-1,-2,-3,-4]
print(first_missing_positive(nums))

nums = [55,22,52,100,1,3,-5]
print(first_missing_positive(nums))

nums = [0,-1,-2,-3,5]
print(first_missing_positive(nums))
