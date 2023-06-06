#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:35:08 2023

@author: johnmorgan
"""

# O(nlog(n)) - using this because sort chapter
# Set, dict fastest at O(n)
# Review binary search code

def find_sum(lst, n):
    lst.sort()
    left = 0
    right = len(lst) - 1
    while left != right:
        curr_sum = lst[left] + lst[right]
        if curr_sum < n:
            left += 1
        elif curr_sum > n:
            right -= 1
        else:
            return [lst[left], lst[right]]
    return -1
    
lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 81
print(find_sum(lst, n))