#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:47:38 2023

@author: johnmorgan
"""

from heapq import *

def kth_smallest_element(matrix, k):
    min_heap = []
    curr = None
    for index in range(len(matrix)):
        heappush(min_heap, (matrix[index][0], index, 0))
    while k > 0:
        if len(min_heap) == 0:
            return curr
        curr = heappop(min_heap)
        if len(matrix[curr[1]]) > curr[2] + 1:
            heappush(min_heap, (matrix[curr[1]][curr[2] + 1], curr[1], curr[2] + 1))
        k -= 1
    return curr[0]
    
matrix = [[2,6,8],[3,7,10],[5,8,11]]
k = 3
print(kth_smallest_element(matrix, k))