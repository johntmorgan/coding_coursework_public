#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:11:56 2023

@author: johnmorgan
"""

from heapq import heappush, heappop
from collections import defaultdict

# O(nlogn) - inserting all elements into heap
# O(n + k) space - hash, heap

def top_k_frequent(arr, k):
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1
    heap = []
    for item in freq.items():
        if len(heap) < k:
            heappush(heap, (item[1], item[0]))
        else:
            if heap[0][0] < item[1]:
                heappush(heap, (item[1], item[0]))
                heappop(heap)
    return [elem for _, elem in heap]

arr = [1, 1, 1, 2, 2, 4, 5, 5]
k = 3
print(top_k_frequent(arr, k))

arr = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10
print(top_k_frequent(arr, k))
