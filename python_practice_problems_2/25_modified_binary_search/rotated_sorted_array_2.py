#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:14:11 2023

@author: johnmorgan
"""

def search(arr, t):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == t:
            return True
        if arr[low] < arr[mid]:
            if arr[mid] > t:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (arr[mid] < t and arr[high] > t):
                low = mid + 1
            else:
                high = mid - 1
    return False


arr = [-14,16,19,22,67]
t = 19
print(search(arr, t))

arr = [2,5,6,0,0,1,2]
t = 0
print(search(arr, t))

arr = [2,5,6,0,0,1,2]
t = 3
print(search(arr, t))

arr = [-13, 3, 12, 13, 19, 57]
t = 19
print(search(arr, t))