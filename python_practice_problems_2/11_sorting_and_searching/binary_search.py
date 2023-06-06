#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 10:59:51 2023

@author: johnmorgan
"""

def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            return mid
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found