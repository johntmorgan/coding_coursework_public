#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:08:18 2023

@author: johnmorgan
"""

# Quick O(n) sol'n

def find_closest(lst, target):
    diff = float('inf')
    result = None
    for elem in lst:
        if abs(target - elem) < diff:
            diff = abs(target - elem)
            result = elem
    return(result)

# O(log(n)) sol'n

def find_closest(lst, target):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return target
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if abs(lst[low] - target) < abs(lst[mid] - target):
        return lst[low]
    return lst[mid]
            

lst = [-9, -4, -2, 0, 1, 3, 4, 10]
target = 5
print(find_closest(lst, target))

lst = [1, 2, 5, 10, 23, 25, 30, 50]
target = 100
print(find_closest(lst, target))

lst = [-9, -4, -2, 0, 1, 3, 4, 10]
target = -10
print(find_closest(lst, target))