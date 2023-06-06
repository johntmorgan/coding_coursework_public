#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:06:37 2023

@author: johnmorgan
"""

# Not bad but review

def print_unique_permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    res = []
    tested = set()
    for index, num in enumerate(nums):
        if num not in tested:
            new_arr = nums[:index] + nums[index + 1:]
            for p in print_unique_permutations(new_arr):
                res.append([num] + p)
            tested.add(num)
    return res