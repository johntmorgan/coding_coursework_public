#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:47:20 2023

@author: johnmorgan
"""

from heapq import *

# O((k + m) * log(m)) - m is number of lists, k is number to find
# Savings vs sorting entire list together
# Space O(n), total number of elements in array - could need to store all

def k_smallest_number(lists, k):
    min_heap = []
    curr = (0, 0)
    for index, list_elem in enumerate(lists):
        if len(lists[index]) > 0:
            list_elem = lists[index].pop(0)
            heappush(min_heap, (list_elem, index))
    while k > 0:
        if len(min_heap) == 0:
            return curr[0]
        curr = heappop(min_heap)
        if len(lists[curr[1]]) > 0:
            heappush(min_heap, (lists[curr[1]].pop(0), curr[1]))
        k -= 1
    return curr[0]

lists = [[2,6,8],[3,7,10],[5,8,11]]
k = 5
print(k_smallest_number(lists, k))