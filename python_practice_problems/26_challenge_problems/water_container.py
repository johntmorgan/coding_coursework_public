#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:14:22 2023

@author: johnmorgan
"""

def container_with_most_water(heights):
    if len(heights) < 2:
        return 0
    left, right = 0, len(heights) - 1
    max_vol = 0
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        max_vol = max(max_vol, height * width)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return max_vol