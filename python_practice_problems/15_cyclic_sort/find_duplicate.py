#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:26:52 2023

@author: johnmorgan
"""

# Naive O(n^2)

def find_duplicate(nums):
    for index1, elem1 in enumerate(nums):
        for index2, elem2 in enumerate(nums):
            if elem1 == elem2 and index1 != index2:
                return elem1

# O(n) cyclic

def find_duplicate(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1:
            j = nums[i] - 1
            if nums[j] == nums[i]:
                return nums[i]
            nums[i], nums[j] = nums[j], nums[i]
            
    
nums = [1,3,4,2,2]
print(find_duplicate(nums))

nums = [3,4,4,4,2]
print(find_duplicate(nums))