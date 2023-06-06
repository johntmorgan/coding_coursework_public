#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:28:46 2023

@author: johnmorgan
"""

def contains_duplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)
    return False

nums = [1,3,6,2,3,5,4,8,7,6,2,3,5,2,9,4,3]
print(contains_duplicate(nums))