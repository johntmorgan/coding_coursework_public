#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:13:56 2023

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