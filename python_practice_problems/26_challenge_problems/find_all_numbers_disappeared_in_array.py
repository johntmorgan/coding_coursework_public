#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:37:27 2023

@author: johnmorgan
"""

def find_disappeared_numbers(nums):
    for i in range(len(nums)):
        if nums[i] > len(nums):
            return False
        while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
            if nums[i] > len(nums):
                return False
    res = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)
    return res


nums = [1,2,5,2,2]
print(find_disappeared_numbers(nums))