#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:26:37 2023

@author: johnmorgan
"""

# Review

def longest_subsequence(nums):
    arr = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                arr[i] = max(arr[i], arr[j] + 1)
    return max(arr)

