#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:31:33 2023

@author: johnmorgan
"""

def rob_houses(nums):
    best = [0] * len(nums)
    for index, house in enumerate(nums):
        if index < 2:
            best[index] = nums[index]
        else:
            best[index] = max(nums[index] + best[index - 2], best[index - 1])
    return best[len(nums) - 1]

nums = [1,2,3,1]
print(rob_houses(nums))