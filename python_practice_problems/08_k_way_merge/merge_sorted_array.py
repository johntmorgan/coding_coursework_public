#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:04:47 2023

@author: johnmorgan
"""

def merge_sorted(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = (m + n) - 1
    while p >= 0:
        print(p, p1, p2)
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    return(nums1)
    
    
# nums1 = [10,49,99,110,176,0,0,0,0,0,0,0,0,0,0,0,0,0]
# n = 5
# nums2 = [1,2,4,7,8,12,15,19,24,50,69,100]
# m = 12
# print(merge_sorted(nums1, m, nums2, n))

# nums1 = [1,2,3,0,0,0]
# n = 3
# nums2 = [4,5,6]
# m = 3
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