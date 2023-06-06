#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:12:18 2023

@author: johnmorgan
"""

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return mid