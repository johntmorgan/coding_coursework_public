#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:53:43 2023

@author: johnmorgan
"""

# Review, got dizzy = find which side is cleanly sorted, then see if there

def search(arr, t):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == t:
            return True
        if arr[mid] < arr[high]:
            if t > arr[mid] and t <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if t < arr[mid] and t >= arr[low]:
                high = mid - 1
            else:
                low = mid + 1    
    return False
    
arr = [22,67,-14,16,19]
t = 19
print(search(arr, t))

arr = [13, 19, 57, -13, 3, 12] 
t = 19
print(search(arr, t))

arr = [6, 0, 0, 1, 2, 2, 5] 
t = 0
print(search(arr, t))