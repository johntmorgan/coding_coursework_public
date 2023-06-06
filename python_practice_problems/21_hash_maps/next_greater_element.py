#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 17:44:15 2023

@author: johnmorgan
"""

# O(n1^2 + n2^2)
# O(n1^2) because O(n) add, O(n) time to add worst case

def next_greater_element(nums1, nums2):
    result = [-1] * len(nums1)
    n1_hash = {}
    for index, elem in enumerate(nums1):
       n1_hash[elem] = index
    for index, elem in enumerate(nums2):
        if elem in n1_hash:
            curr, found = index, False
            while not found and index < len(nums2):
                if nums2[index] > elem:
                    found = True
                    result_index = n1_hash[elem]
                    result[result_index] = nums2[index]
                if not found:
                    index += 1
    return result


nums1 = [5, 4, 7]
nums2 = [4, 5, 7, 3]
print(next_greater_element(nums1, nums2))