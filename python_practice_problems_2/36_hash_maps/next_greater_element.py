#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:27:08 2023

@author: johnmorgan
"""

# Naive search one at a time - O(n1 * n2)

# Add to hash map O(n1) average - worst case O(n1^2)
# Iterating over n2 worst case O(n2^2)
# O(n1^2 + n2^2) -> O(n2^2) as n2 > n1
# Space complexity O(n1) for hash map

def next_greater_element(nums1, nums2):
    result = [-1] * len(nums1)
    n1_map = {}
    for index, elem in enumerate(nums1):
        n1_map[elem] = index
    for index, elem in enumerate(nums2):
        if elem in n1_map.keys():
            while index < len(nums2) and nums2[index] <= elem:
                index += 1
            if index != len(nums2):
                result[n1_map[elem]] = nums2[index]
    return result

nums1 = [2,4]
nums2 = [1,2,3,4]
print(next_greater_element(nums1, nums2))

nums1 = [1, 3]
nums2 = [1,2,3,4]
print(next_greater_element(nums1, nums2))