#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:40:50 2023

@author: johnmorgan
"""

def first_k_missing_numbers(nums, k):
    for i in range(len(nums)):
        while 0 < nums[i] < len(nums) and nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1 and k > 0:
            missing.append(i + 1)
            k -= 1
    if k > 0:
        start = len(nums)
        while k > 0:
            start += 1
            missing.append(start)
            k -= 1
    return missing
            

nums = [0,-5,1,3,5,4]
k = 3
print(first_k_missing_numbers(nums, k))