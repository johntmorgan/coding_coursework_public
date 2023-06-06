#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 16:27:17 2023

@author: johnmorgan
"""

# Review, recursion called from for loop

def print_unique_permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return[nums]
    res = []
    tested = set()
    for index, num in enumerate(nums):
        if num not in tested:
            new_arr = nums[0:index] + nums[index + 1:]
            for p in print_unique_permutations(new_arr):
                res.append([num] + p)
            tested.add(num)
    return res
    

nums = [4,2,4]
print(print_unique_permutations(nums))
nums = [3,2,5]
print(print_unique_permutations(nums))
nums = [4,3,2,5]
print(print_unique_permutations(nums))