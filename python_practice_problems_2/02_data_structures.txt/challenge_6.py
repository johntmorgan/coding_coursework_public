#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:08:53 2023

@author: johnmorgan
"""

# Quick and dirty O(n^2)

def find_first_unique(lst):
    for idx in range(len(lst)):
        if lst[idx] not in lst[:idx] + lst[idx + 1:]:
            return lst[idx]
    return None

# O(n) with hashing fun - not allowed yet in this course tho

def find_first_unique(lst):
    occur_dict = {}
    for elem in lst:
        if elem in occur_dict:
            occur_dict[elem] = occur_dict[elem] + 1
        else:
            occur_dict[elem] = 1
    for elem in lst:
        if occur_dict[elem] == 1:
            return elem
    return None

# Sort O(nlogn) - wrong, need first elem in unsorted list

# def find_first_unique(lst):
#     lst.sort()
#     for idx in range(len(lst)):
#         if idx == 0 and lst[idx + 1] != lst[idx]:
#             return lst[idx]
#         elif idx == len(lst) - 1 and lst[idx - 1] != lst[idx]:
#             return lst[idx]
#         else:
#             if lst[idx + 1] != lst[idx] and lst[idx - 1] != lst[idx]:
#                 return lst[idx]


unique_list = [9,2,3,2,6,6]
print(find_first_unique(unique_list))
unique_list_2 = [2,3,2,6,9,6]
print(find_first_unique(unique_list_2))
unique_list_3 = [2,2,6,9,6]
print(find_first_unique(unique_list_3))