#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:23:54 2023

@author: johnmorgan
"""

# Copied solution, didn't get it
# Swap first half of second segment with second half of first segment
# Recurse on both segments

import math

def shuffle_list_recursive(lst, left, right):
    # Base case: If there are more than 2 elements are remaining
    if right - left > 1:
        mid = (left + right) // 2  # Compute mid of the list
        temp = mid + 1  # First half of the second list
        middle = (left + mid) // 2  # Second half of the first list

        # Swapping elements of the sub-list
        for i in range(middle + 1, mid+1):
            lst[i], lst[temp] = lst[temp], lst[i]
            temp += 1

        # Recursively pass the first and second half of the list
        shuffle_list_recursive(lst, left, mid)
        shuffle_list_recursive(lst, mid + 1, right)

# JM ver redo

def shuffle_list_recursive(lst, left, right):
    if right - left > 1:
        mid_list = (left + right) // 2
        temp = mid_list + 1
        mid_first = (left + mid_list) // 2
        for i in range(mid_first + 1, mid_list + 1):
            lst[i], lst[temp] = lst[temp], lst[i]
            temp += 1
        shuffle_list_recursive(lst, left, mid_list)
        shuffle_list_recursive(lst, mid_list + 1, right)

def shuffle_list(lst):
    lst_len = len(lst)
    while lst_len > 1:
        if lst_len % 2 == 0:
            lst_len = lst_len / 2
        else:
            return lst
    shuffle_list_recursive(lst, 0, len(lst) - 1)
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(shuffle_list(lst))

lst = [1, 2, 3, 4, 5, 6, 7]
print(shuffle_list(lst))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle_list(lst))