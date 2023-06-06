#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 13:18:42 2023

@author: johnmorgan
"""

# Review again
# Initialize array to calc max subsequence at each location
# In each location, look at all prior locations
# If location > prior_location, append (loc val  = prior val + 1) or keep current
# Update max for whole array after finding best for location
# Do not just return last result - may not include it

def longest_subsequence(nums):
    dp = [1] * len(nums)
    res = 1
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res


nums = [10,9,2,5,3,7,101,18]
print(longest_subsequence(nums))