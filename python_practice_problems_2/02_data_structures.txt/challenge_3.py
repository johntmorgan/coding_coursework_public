#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 3 14:28:22 2023

@author: johnmorgan
"""

# Not good, can result in duplicate numbers summing

# def find_sum(lst, k):
#     for first in lst:
#         for second in lst:
#             if first + second == k:
#                 return [first, second]
#     return "Not found"

# Simple but slow, O(n^2)

# def find_sum(lst, k):
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if lst[i] + lst[j] == k and i != j:
#                 return [lst[i], lst[j]]
#     return "Not found"

# O(nlogn) - sort then binary search
# Sort takes O(nlogn)
# Search takes n * O(logn) -> O(nlogn)

# def binary_search(a, item):
#     first = 0
#     last = len(a) - 1
#     found = False
#     index = -1
#     while first <= last and not found:
#         mid = (first + last) // 2
#         if a[mid] == item:
#             index = mid
#             found = True
#         else:
#             if item < a[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     if found:
#         return index
#     else:
#         return -1

def binary_search(a, item):
    first = 0
    last = len(a) - 1
    while first < last:
        mid = (first + last) // 2
        if a[mid] == item:
            return mid
        elif item < a[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return -1

def find_sum(lst, k):
    lst.sort() # O(nlogn) time
    for j in range(len(lst)):
        index = binary_search(lst, k - lst[j])
        if index != -1 and index is not j:
            return [lst[j], k - lst[j]]

# Moving indices
# Sort takes O(nlogn), search takes O(n)

# def find_sum(lst, k):
#     lst.sort()
#     idx1 = 0
#     idx2 = len(lst) - 1
#     while idx1 != idx2:
#         curr_sum = lst[idx1] + lst[idx2]
#         if curr_sum > k:
#             idx2 -= 1
#         elif curr_sum < k:
#             idx1 += 1
#         else:
#             return([lst[idx1], lst[idx2]])

# Best, but not "learned" yet - will see in hashing chapters

# def find_sum(lst, k):
#     sum_dict = {}
#     for first in lst:
#         if first in sum_dict:
#             return [first, sum_dict[first]]
#         else:
#             sum_dict[k - first] = first
#     return "Not found"
        
lst = [1,21,3,14,5,60,7,6]
k = 81

print(find_sum(lst, k))