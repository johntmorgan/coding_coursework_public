#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:01:14 2023

@author: johnmorgan
"""

from heapq import *

def k_smallest_pairs(list1, list2, k):
    pair_heap = []
    result = []
    p2 = 1
    for index, elem in enumerate(list1):
        heappush(pair_heap, (elem + list2[0], index, 0))
    while len(result) < k:
        small = heappop(pair_heap)
        result.append([list1[small[1]], list2[small[2]]])
        if p2 > len(list2) - 1:
            while len(pair_heap) > 0 and len(result) < k:
                small = heappop(pair_heap)
                result.append([list1[small[1]], list2[small[2]]])
            return result
        if len(pair_heap) == 0 or list2[p2] + list1[0] < pair_heap[0][0]:
            for index, elem in enumerate(list1):
                heappush(pair_heap, (elem + list2[p2], index, p2))   
            p2 += 1
    return result

print(k_smallest_pairs([1, 1, 2] , [1, 2, 3] , 4))

print(k_smallest_pairs([1, 2, 300] , [1, 11, 20, 35, 300] , 30))