#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:49:09 2023

@author: johnmorgan
"""

# Recursive solution, with no memoization

def recur_steal(nums, can_steal, loc):
    if loc >= len(nums):
        return 0
    else:
        if can_steal:
            loot = max((nums[loc] + recur_steal(nums, False, loc + 1)), 
                       recur_steal(nums, True, loc + 1))
        else:
            loot = recur_steal(nums, True, loc + 1)
    return loot
    
def rob_houses(nums):
    return recur_steal(nums, True, 0)

# Dynamic programming solution, O(n)

def rob_houses(nums):
    n = len(nums)
    can_steal = True
    arr = [0] * n
    arr[0] = nums[0]
    arr[1] = nums[1]
    for i in range(2, n):
        arr[i] = max(nums[i] + arr[i - 2], arr[i - 1])
    return arr[n - 1]


nums = [0,1,2,5] #6
print(rob_houses(nums))
nums = [2,7,9,3,1] #12
print(rob_houses(nums))
nums = [3,6,1,2,4] #10
print(rob_houses(nums))