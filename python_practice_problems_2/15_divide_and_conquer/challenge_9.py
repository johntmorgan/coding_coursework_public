#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:00:11 2023

@author: johnmorgan
"""

# Quick O(n^2)

def inversion_count(lst):
    inversion_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                inversion_count +=1
    return inversion_count

# Faster, copy from solution
# O(nlogn)) - basically modified merge
# Review again!

def inversion_count(lst, n):
    temp = [0]*n
    return ic_recursive(lst, temp, 0, n-1)
 
def ic_recursive(lst, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += ic_recursive(lst, temp, 
                                    left, mid)
        inv_count += ic_recursive(lst, temp, mid + 1, right)
        inv_count += find_inversion_count(lst, temp, left, mid, right)
    return inv_count

def find_inversion_count(lst, temp, left, mid, right):
    i = left     # Left sublist starting index
    j = mid + 1  # Right sublist starting index
    k = left     # Sorted sublist starting index
    inv_count = 0     # Store inversion counts in each recursive call 
 
    while i <= mid and j <= right:
        if lst[i] <= lst[j]:
            temp[k] = lst[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp[k] = lst[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp[k] = lst[i]
        k += 1
        i += 1
 
    while j <= right:
        temp[k] = lst[j]
        k += 1
        j += 1
 
    # The sorted sublist copied into original list
    for index in range(left, right + 1):
        lst[index] = temp[index]
    return inv_count


lst = [7, 6, 5, 8]
print(inversion_count(lst))

lst = [9, 5, 6, 11, 8, 10]
print(inversion_count(lst))