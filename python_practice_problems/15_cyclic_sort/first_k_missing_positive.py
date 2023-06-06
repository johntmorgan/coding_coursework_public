#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:11:27 2023

@author: johnmorgan
"""

# Gets stuck on submission, even though all test cases working...
# No error message to debug

def first_k_missing_numbers(nums, k):
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[i] > 0 and nums[i] <= len(nums):
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    res = []
    i = 0
    while k > 0 and i < len(nums):
        if nums[i] != i + 1:
            res.append(i + 1)
            k -= 1
        i += 1
    start = len(nums) + 1
    while k > 0:
        res.append(start)
        start += 1
        k -= 1
    return res
            

nums = [0,-5,1,3,5,4]
k = 3
print(first_k_missing_numbers(nums, k))

nums = [1,2,3,4,5]
k = 6
print(first_k_missing_numbers(nums, k))

nums = [1,-1,2]
k = 2
print(first_k_missing_numbers(nums, k))

nums = []
k = 2
print(first_k_missing_numbers(nums, k))

nums = [0]
k = 2
print(first_k_missing_numbers(nums, k))

nums = [-1, -2]
k = 2
print(first_k_missing_numbers(nums, k))

nums = [1, 2]
k = 2
print(first_k_missing_numbers(nums, k))

nums = [5, 6]
k = 2
print(first_k_missing_numbers(nums, k))

nums = [-6, 6]
k = 2
print(first_k_missing_numbers(nums, k))

nums = [1, 2, 3, 0, 4, 9, 7]
k = 4
print(first_k_missing_numbers(nums, k))

nums = [-1, 2, -8, -3, 4, -7, 6, 3]
k = 5
print(first_k_missing_numbers(nums, k))

nums = [2, 0, 9, 1, 5, 6, 8, 12, -9, 3, 4]
k = 10
print(first_k_missing_numbers(nums, k))