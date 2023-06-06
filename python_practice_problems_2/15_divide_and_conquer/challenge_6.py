#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:40:22 2023

@author: johnmorgan
"""

# Fast but O(n)

# def missing_number(lst):
#     for i in range(len(lst)):
#         if lst[i] != i + 1:
#             return i + 1
#     return -1

# O(logn)

def mn_recurse(lst, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    if mid == len(lst) - 1:
        if lst[mid] == len(lst):
            return -1
        else:
            return len(lst) - 1
    if mid == 0:
        if lst[mid] == 1:
            return -1
        else:
            return 1
    if lst[mid + 1] - lst[mid - 1] > 2:
        if lst[mid] - lst[mid - 1] == 2:
            return lst[mid] - 1
        else:
            return lst[mid] + 1
    if lst[mid] == mid + 1:
        return mn_recurse(lst, mid + 1, high)
    else:
        return mn_recurse(lst, low, mid - 1)

def missing_number(lst):
    return mn_recurse(lst, 0, len(lst) - 1)

# Cleaner course solution

def missing_number(lst):
    left_limit = 0 # Start of the list
    right_limit = len(lst) - 1 # End of the list

    # Keeping in check the boundary case
    if lst[left_limit] is not 1: # If 1 is not present at 0th index
        return 1

    # Binary Search
    while left_limit <= right_limit:
        middle = (left_limit + right_limit) // 2 # Finding mid

        # Element at index `i` should be `i+1` (e.g. 1 at index 0). If this is the first element  which is not `i`+ 1,
        # then  missing element is middle + 1
        if lst[middle] is not middle + 1 and lst[middle -1] is middle:
            return middle + 1

        # If this is not the first missing number then search in left sub-list
        if lst[middle] is not middle + 1:
            right_limit = middle - 1
        # If it follows index + 1 property then search in right side of the list
        else:
            left_limit = middle + 1
    return -1 # If there is no missing number

lst = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(missing_number(lst))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(missing_number(lst))

lst = [1, 2, 4]
print(missing_number(lst))