#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:16:34 2023

@author: johnmorgan
"""

# Simple O(n)

def find_minimum(arr):
    if len(arr) == 0:
        return None
    min_val = arr[0]
    for elem in arr:
        if elem < min_val:
            min_val = elem
    return min_val

# Worse but for fun O(nlogn)

def find_minimum(arr):
    arr.sort()
    return(arr[0])


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # For all the remaining values
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k]=right[j]
            j += 1
            k += 1


def find_minimum(arr):
    if len(arr) == 0:
        return None
    merge_sort(arr)
    return(arr[0])

# Recursively find min of both sides, for fun

# def find_minimum(arr):
#     if len(arr) == 2:
#         if arr[0] < arr[1]:
#             return arr[0]
#         else:
#             return arr[1]
#     elif len(arr) == 1:
#         return arr[0]
#     else:
#         split = len(arr) // 2
#         first_half = find_minimum(arr[:split])
#         second_half = find_minimum(arr[split:])
#         if first_half < second_half:
#             return first_half
#         else:
#             return second_half

arr = [9,2,3,6]
print(find_minimum(arr))