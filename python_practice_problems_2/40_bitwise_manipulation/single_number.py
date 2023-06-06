#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:42:20 2023

@author: johnmorgan
"""

# O(n) time, iterate over array
# O(1) space

def single_number(nums):
    result = 0
    for num in nums:
        result = result ^ num # result ^= num works 
    return result

nums = [1,2,2,3,3,1,4]
print(single_number(nums))