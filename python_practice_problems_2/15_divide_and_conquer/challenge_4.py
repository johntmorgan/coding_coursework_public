#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:40:39 2023

@author: johnmorgan
"""

# Course answer, did not get on own
# O(n * h) where h is highest stack of coins
# Review

def ms_recursive(lst, left, right, h):
    if left >= right:
        return 0
    min_height = left
    for i in range(left, right):
        if lst[i] < lst[min_height]:
            min_height = i
    # Collect all vertical = right - left vs
    # Divide at min_height and collect left and right, collecting rows up to min_height
    return min(right - left, ms_recursive(lst, left, min_height, lst[min_height])
               + ms_recursive(lst, min_height + 1, right, lst[min_height]) +
               lst[min_height] - h)

def minimum_steps(lst):
    steps = 0
    ms_recursive(lst, 0, len(lst), 0)


lst = [2, 5, 1, 2, 3, 1]
print(minimum_steps(lst))