#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:26:32 2023

@author: johnmorgan
"""

from heapq import *

# O(k) initial insert
# O((n - k) * (logk)
# O(k) space

def find_kth_largest(arr, k):
    minh = []
    index = 0
    while k > 0:
        heappush(minh, arr[index])
        index += 1
        k -= 1
    print(minh)
    for index in range(index, len(arr)):
        elem = arr[index]
        if elem > minh[0]:
            heappop(minh)
            heappush(minh, elem)
    return minh[0]

arr = [-1,-5,-9,-11,-5,-10,-3,-4,-1,-12,-13,-8]
k = 7
print(find_kth_largest(arr, k))