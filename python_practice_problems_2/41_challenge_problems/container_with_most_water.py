#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 18:12:56 2023

@author: johnmorgan
"""

# O(n), best
# Look at stack solution too?

def container_with_most_water(heights):
    left, right = 0, len(heights) - 1
    max_vol = 0
    while left != right:
        vol = min(heights[left], heights[right]) * (right - left)
        if vol > max_vol:
            max_vol = vol
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return max_vol

heights = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(heights))