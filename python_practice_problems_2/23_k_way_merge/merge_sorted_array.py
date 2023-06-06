#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:47:50 2023

@author: johnmorgan
"""

from traversal import *

# O(n + m)
# O(1) space

# Tip: You may use some of the code templates provided
# in the support file

def merge_sorted(nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    p = len(nums1) - 1
    while p >= 0:
        if p1 < 0:
            nums1[p] = nums2[p2]
            p2 -= 1
        elif p2 < 0:
            nums1[p] = nums1[p1]
            p1 -= 1  
        elif nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    return nums1


# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [4,5,6]
# n = 3
# print(merge_sorted(nums1, m, nums2, n))

# nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
# m = 5 
# nums2 = [-1, -1, 0, 0, 1, 2]
# n = 6
# print(merge_sorted(nums1, m, nums2, n))

nums1 = [6, 7, 8, 9, 10, 0, 0, 0, 0, 0]
m = 5
nums2 = [1, 2, 3, 4, 5]
n = 5
print(merge_sorted(nums1, m, nums2, n))