#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:05:45 2023

@author: johnmorgan
"""

from collections import deque

# Space O(window_size)

def find_max_sliding_window(nums, window_size):
    window = deque(nums[:window_size])
    output = [max(window)]
    for i in range(window_size, len(nums)):
        window.popleft()
        window.append(nums[i])
        output.append(max(window))
    return output

# GPT-4 though
def find_max_sliding_window(nums, window_size):
    output = [max(nums[i:i+window_size]) for i in range(len(nums) - window_size + 1)]
    

nums = [1,2,3,4,5,6,7,8,9,10]
window_size = 3
print(find_max_sliding_window(nums, window_size))