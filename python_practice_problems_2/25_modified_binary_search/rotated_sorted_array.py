#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:11:42 2023

@author: johnmorgan
"""

# O(logns)
# O(1) space

def binary_search_rotated(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] < nums[mid]:
            if target < nums[mid] and target >= nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target > nums[mid] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [6,7,1,2,3,4,5]
target = 3
print(binary_search_rotated(nums, target))

nums = [4, 5, 6, 1, 2, 3]
target = 3
print(binary_search_rotated(nums, target))
