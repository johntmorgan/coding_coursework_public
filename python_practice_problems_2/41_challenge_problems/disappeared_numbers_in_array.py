#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:43:16 2023

@author: johnmorgan
"""

# Sort and return non-matching array positions - O(nlogn), O(sorting)
# Store in hash map, then go through and look for missing key O(n), O(n)
# Cyclic sort, O(n), O(1) - review

# Sorting

# def find_disappeared_numbers(nums):
#     nums.sort()
#     res = []
#     for index, num in enumerate(nums):
#         if num != index + 1:
#             res.append(index + 1)
#     return res

# Sorting

# def find_disappeared_numbers(nums):
#     res = []
#     s = set()
#     for num in nums:
#         if num not in s:
#             s.add(num)
#     for target in range(1, len(nums) + 1):
#         if target not in s:
#             res.append(target)
#     return res

# Cyclic sorting

def find_disappeared_numbers(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] > len(nums):
            return False
        if nums[i] != i + 1 and nums[i] < len(nums):
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]
    for target in range(1, len(nums) + 1):
        if target not in nums:
            res.append(target)
    return res

nums = [1,2,5,2,2]
print(find_disappeared_numbers(nums))