#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:30:09 2023

@author: johnmorgan
"""

from heapq import *

# O((n+k)logn)

def kth_smallest_element(matrix, k):
    minh = []
    for index in range(len(matrix)):
        heappush(minh, [matrix[index][0], index, 0])
    while k > 0:
        elem = heappop(minh)
        if len(matrix[elem[1]]) - 1 > elem[2]:
            heappush(minh, [matrix[elem[1]][elem[2] + 1], elem[1], elem[2] + 1])
        # print(elem[0])
        k -= 1
    return elem[0]
    

# matrix = [[2,6,8],[3,7,10],[5,8,11]]
# k = 3
# print(kth_smallest_element(matrix, k))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 4
print(kth_smallest_element(matrix, k))
