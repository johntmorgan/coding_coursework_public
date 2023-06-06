#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:44:26 2023

@author: johnmorgan
"""

def find_corrupt_pair(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [i + 1, nums[i]]
    

nums = [3,1,2,5,2]
print(find_corrupt_pair(nums))