#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:55:11 2023

@author: johnmorgan
"""

def find_min(nums):
    left, right = 0, len(nums) - 1
    mid = None
    while left <= right:
        mid = (left + right) // 2
        if nums[right] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if mid < len(nums) - 1:
        return min(nums[mid], nums[mid + 1])
    else:
        return nums[mid]

nums = [5,7,17,21,22,2,4]
print(find_min(nums))

nums = [-17, -2, -1, 0, 12, 15, 100, 121, 289]
print(find_min(nums))

nums = [-2, -1, 0, 12, 15, 100, 121, 289, -17]
print(find_min(nums))