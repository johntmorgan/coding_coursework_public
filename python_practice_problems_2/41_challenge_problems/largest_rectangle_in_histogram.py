#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:30:49 2023

@author: johnmorgan
"""

# Works but clumsy O(n^2) not using stack

def largest_rectangle(heights):
    best = 0
    avail_heights = []
    for height in heights:
        for index, avail_height in enumerate(avail_heights):
            if avail_height[0] > height:
                avail_height[0] = height
                avail_height[1] += 1
            else:
                avail_height[1] += 1
        avail_heights.append([height, 1])
        for avail_height in avail_heights:
            if avail_height[0] * avail_height[1] > best:
                best = avail_height[0] * avail_height[1]
    return best

# Review
# O(n) using stack

def largest_rectangle(heights):
    stack, ans = [], 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            ans = max(ans, H*W)
        stack.append(i)
        print(stack)
    return ans

heights = [6,2,5,4,5,1,6,4,2]
print(largest_rectangle(heights)) # 12

heights = [16,22,2,45,19,33,11,28]
print(largest_rectangle(heights)) # 57