#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:52:56 2023

@author: johnmorgan
"""

def find_duplicates(nums):
    for i, num in enumerate(nums):
        while nums[i] <= len(nums) and nums[i] != i + 1 and \
            nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    print(nums)
    res = []
    for i, num in enumerate(nums):
        if nums[i] != i + 1 and nums[i] not in res:
            res.append(nums[i])
    return res

nums = [4,3,2,7,8,2,3,1]
print(find_duplicates(nums))