#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:38:59 2023

@author: johnmorgan
"""

def find_majority_element(nums):
    l_nums = len(nums)
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
            if freq[num] >= len(nums) / 2:
                return num
        else:
            freq[num] = 1
    return None

nums = [1,2,1,1,1]
print(find_majority_element(nums))

nums = [7, 7, 5, 5, 7, 5, 7, 5, 7, 5, 7, 5, 7, 7, 5, 5, 7, 5, 5]
print(find_majority_element(nums))