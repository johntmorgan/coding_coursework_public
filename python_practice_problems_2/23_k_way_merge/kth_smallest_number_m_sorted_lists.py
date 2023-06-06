#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:07:37 2023

@author: johnmorgan
"""

from heapq import *

# O(klogn) time complexity
# O(n) space complexity

def k_smallest_number(lists, k):
    heap = []
    if len(lists[0]) == 0:
        return 0
    for index in range(len(lists)):
        heappush(heap, [lists[index][0], index, 0])
    while k > 0:
        if len(heap) > 0:
            result = heappop(heap)
            if result[2] < len(lists[result[1]]) - 1:
                heappush(heap, [lists[result[1]][result[2] + 1], result[1], result[2] + 1])
            k -= 1
        else:
            return result[0]
    return result[0]

lists = [[2,6,8],[3,7,10],[5,8,11]]
k = 5
print(k_smallest_number(lists, k))