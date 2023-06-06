#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:49:08 2023

@author: johnmorgan
"""

# Review, was a little clumsy

def binary_search_rotated(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] < target:
                if nums[high] < target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
    return -1
                

nums = [6,7,1,2,3,4,5]
target = 3
print(binary_search_rotated(nums, target))

nums = [4, 5, 6, 1, 2, 3]
target = 3
print(binary_search_rotated(nums, target))