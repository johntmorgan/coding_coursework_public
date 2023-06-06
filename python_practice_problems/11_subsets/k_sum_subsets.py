#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:24:31 2023

@author: johnmorgan
"""

def get_k_sum_subsets(nums, target):
    subsets = [[]]
    for index in range(len(nums)):
        for sub_index in range(len(subsets)):
            subsets.append(subsets[sub_index] + [nums[index]])
    result = []
    for subset in subsets:
        if sum(subset) == target:
            result.append(subset)
    return result

nums = [8,13,3,22,17,39,87,45,36]
target = 47
print(get_k_sum_subsets(nums, target))