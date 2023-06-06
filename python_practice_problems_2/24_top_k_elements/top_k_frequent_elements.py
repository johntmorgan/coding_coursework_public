#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:15:13 2023

@author: johnmorgan
"""

from heapq import heappush, heappop

# O(nlogk)
# O(n + k) space - hash + heap

def top_k_frequent(arr, k):
    d = {}
    for elem in arr:
        if elem in d:
            d[elem] = d[elem] + 1
        else:
            d[elem] = 1
    minh = []
    for key, value in d.items():
        if len(minh) < k:
            heappush(minh, [value, key])
        else:
            if value > minh[0][0]:
                heappop(minh)
                heappush(minh, [value, key])
    result = []
    for vk_pair in minh:
        result.append(vk_pair[1])
    return result

arr = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10
print(top_k_frequent(arr, k))