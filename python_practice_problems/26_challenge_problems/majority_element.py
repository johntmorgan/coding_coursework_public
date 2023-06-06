#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:44:47 2023

@author: johnmorgan
"""

def find_majority_element(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for key in freq:
        if freq[key] > len(nums) // 2:
            return key