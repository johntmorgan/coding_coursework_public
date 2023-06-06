#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:26:27 2023

@author: johnmorgan
"""

# O(n) solution, review

def largest_rectangle(heights):
    stack = [-1]
    best = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            curr_height = heights[stack.pop()]
            curr_width = i - stack[-1] - 1
            best = max(best, curr_height * curr_width)
        stack.append(i)
    while stack[-1] != -1:
        curr_height = heights[stack.pop()]
        curr_width = len(heights) - stack[-1] - 1
        best = max(best, curr_height * curr_width)
    return best


# heights = [4,5,12,2]
# print(largest_rectangle(heights))

heights = [6, 2, 5, 4, 5, 1, 6, 4, 2]
print(largest_rectangle(heights))