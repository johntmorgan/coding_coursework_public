#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:22:30 2023

@author: johnmorgan
"""

from heapq import *

def find_kth_largest(arr, k):
    heap = []
    for index in range(0, k):
        heappush(heap, arr[index])
    for index in range(k, len(arr)):
        if arr[index] > heap[0]:
            heappush(heap, arr[index])
            heappop(heap)
    return heap[0]
    
    
arr = [-2, 8, 0, -5, 7, -1, 3, -3, -4, 1, 4]
k = 6
print(find_kth_largest(arr, k))