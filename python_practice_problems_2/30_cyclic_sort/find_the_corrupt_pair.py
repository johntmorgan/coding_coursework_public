#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 17:22:15 2023

@author: johnmorgan
"""

# O(n) time, O(1) space

def find_corrupt_pair(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [i + 1, nums[i]]
    return []

nums = [3,1,2,5,2]
print(find_corrupt_pair(nums))