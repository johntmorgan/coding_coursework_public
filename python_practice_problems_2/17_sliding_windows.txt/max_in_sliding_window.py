#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:44:12 2023

@author: johnmorgan
"""

from collections import deque

# Naive
# O(n * w)

def find_max_sliding_window(nums, window_size):
    window = deque()
    result = []
    while len(window) < window_size:
        window.append(nums.pop(0))
    while nums:
        result.append(max(window))
        window.popleft()
        window.append(nums.pop(0))
    result.append(max(window))
    return result

# Course solution retyped by JM w/added notes
# Window maintains index of max element
# O(n)
# Seems like O(n * w)
# But cleanup loop does not run that often!
# Increasing values? Must pop all the first time. But then pop only once
# O(w + n - w) = O(n)
# Decreasing values? Simply popleft as window moves O(n - w)
# Constant values? Also simply popleft as window moves O(n - w)
# Mix? See above, plus increase after constant/decrease incurs O(w) to clean out window
# But this can only happen n/w times worst case
# O(n - n/w + n/w * w) = O(n)
# Space complexity O(w) where w is window size

def find_max_sliding_window(nums, window_size):
    result = []
    window = deque()
    if window_size > len(nums):
        window_size = len(nums)
    for i in range(window_size):
        while window and nums[i] > nums[window[-1]]:
            # Toss smaller, earlier numbers from window
            window.pop()
        # Append last elem to window, always
        window.append(i)
    result.append(nums[window[0]])
    for i in range(window_size, len(nums)):
        # Toss smaller, earlier numbers from window
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        # Toss old big element from window
        if window and window[0] <= (i - window_size):
            window.popleft()
        window.append(i)
        result.append(nums[window[0]])
    return result

nums, window_size = [1,2,3,4,5,6,7,8,9,10] , 3
print(find_max_sliding_window(nums, window_size))
nums, window_size = [3,3,3,3,3,3,3,3,3,3] , 4
print(find_max_sliding_window(nums, window_size))
nums, window_size = [10,6,9,-3,29,-1,34,56,67,-1,-4,-8,-2,9,10,34,67] , 3
print(find_max_sliding_window(nums, window_size))
# nums, window_size = [4,5,6,1,2,3] , 1
# print(find_max_sliding_window(nums, window_size))
# nums, window_size = [9,5,3,1,6,3] , 2
# print(find_max_sliding_window(nums, window_size))
# nums, window_size = [1,2] , 2
# print(find_max_sliding_window(nums, window_size))