#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:56:58 2023

@author: johnmorgan
"""

# O(n), not good

def pivoted_binary_search(lst, n, key):
    rotation = 0
    while lst[n - 1] < lst[0]:
        lst.insert(0, lst.pop())
        rotation += 1
    first = 0
    last = len(lst) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == key:
            found = True
        else:
            if key < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return (mid - rotation + n) % n
    return "Not in list"

# O(log(n))
# Use binary search to find pivot
# Then use binary search on sublist

def pivoted_binary_search(lst, n, key):
    pivot = find_pivot_point(lst, 0, n - 1)
    if pivot == -1:
        return binary_search(lst, 0, n - 1, key)
    if lst[pivot] == key:
        return pivot
    if lst[0] <= key:
        return binary_search(lst, 0, pivot - 1, key)
    return binary_search(lst, pivot + 1, n - 1, key)

def find_pivot_point(lst, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    mid = (low + high) // 2
    if mid < high and lst[mid] > lst[mid + 1]:
        return mid
    if mid > low  and lst[mid] < lst[mid - 1]:
        return mid - 1
    if lst[low] >= lst[mid]:
        return find_pivot_point(lst, low, mid - 1)
    return find_pivot_point(lst, mid + 1, high)
        
def binary_search(lst, low, high, key):
    if high < low:
        return -1
    mid = (low + high) // 2
    if key == lst[mid]:
        return mid
    if key > lst[mid]:
        return binary_search(lst, (mid + 1), high, key)
    return binary_search(lst, low, (mid - 1), key)

lst = [7, 8, 9, 0, 3, 5, 6]
n = len(lst)
key = 3 # Element that is being searched for
print(pivoted_binary_search(lst, n, key))