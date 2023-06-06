#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:21:25 2023

@author: johnmorgan
"""

# Description seems to be off, no solution to check

def find_median(nums1, nums2):
    if len(nums1) >= len(nums2):
        long = nums1
        short = nums2
    else:
        long = nums2
        short = nums1
    if len(long) % 2 == 0:
        left_long = len(long) // 2 - 1
    else:
        left_long = len(long) // 2
    right_long = left_long + 1
    if len(short) % 2 == 0:
        left_short = len(short) // 2 - 1
    else:
        left_short = len(short) // 2
    right_short = left_short + 1
    while not ((long[left_long] < short[right_short] and \
               short[left_short] < long[right_long]) or \
               (left_long == 0 or left_short == 0)):
        if long[left_long] > short[right_short]:
            left_long = left_long // 2
            right_long = left_long + 1
        else:
            left_short = left_short // 2
            right_short = left_short + 1
    print(max(long[left_long], short[left_short]))
    print(min(short[right_short], long[right_long]))
    return (max(long[left_long], short[left_short]) + \
            min(short[right_short], long[right_long])) / 2

nums1 = [1,5,8]
nums2 = [4,7,9]
print(find_median(nums1, nums2))

# nums1 = [1,2]
# nums2 = [3,4]
# print(find_median(nums1, nums2))

# nums1 = [2,4,6,8,10,12]
# nums2 = [1,3,5,7,9,11]
# print(find_median(nums1, nums2))

# nums1 = [5,7,8,13,17,22,29]
# nums2 = [30,32,39,41]
# print(find_median(nums1, nums2))