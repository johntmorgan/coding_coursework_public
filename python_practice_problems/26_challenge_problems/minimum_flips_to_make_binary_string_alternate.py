#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:44:32 2023

@author: johnmorgan
"""

def min_flips(s):
    n = len(s)
    flip_count = 0
    curr_bit = 0
    for c in s:
        if int(c) != curr_bit:
            flip_count += 1
        curr_bit = not curr_bit
    # Either you started the best way, or the inverse would be better
    min_diff = min(flip_count, n - flip_count)
    # Rotating does nothing to even length strings
    # But for odds, if the beginning is different than the end, then
    # rotating helps
    if n % 2 != 0:
        for c in s:
            if int(c) == curr_bit:
                flip_count -= 1
            else:
                flip_count += 1
            min_diff = min(min_diff, flip_count, n - flip_count)
            curr_bit = not curr_bit
    return min_diff
            
s = "110011011"
print(min_flips(s))