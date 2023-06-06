#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:54:10 2023

@author: johnmorgan
"""

# O(log(n + m)) time

def find_median(nums1, nums2):
    if len(nums1) >= len(nums2):
        long, short = nums1, nums2
    else:
        long, short = nums2, nums1
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
    return (max(long[left_long], short[left_short]) + \
            min(short[right_short], long[right_long])) / 2

print(find_median([1,2], [3,4]))
print(find_median([1,5,8], [4,7,9]))