#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:29:34 2023

@author: johnmorgan
"""

from heapq import *

# Time O(m + k)logm
# Space complexity O(m), m = min(k, n1)

def k_smallest_pairs(list1, list2, k):
    pair_heap = []
    result = []
    index2 = 1
    for elem in list1:
        heappush(pair_heap, [elem + list2[0], elem, list2[0]])
    while k > 0 and len(pair_heap) > 0:
        smallest = heappop(pair_heap)
        result.append([smallest[1], smallest[2]])
        if index2 < len(list2):
            for elem in list1:
                heappush(pair_heap, [elem + list2[index2], elem, list2[index2]])
            index2 += 1
        k -= 1
    return result

lst1 = [1,2,300]
lst2 = [1,11,20,35,300]
k = 3
print(k_smallest_pairs(lst1, lst2, k))