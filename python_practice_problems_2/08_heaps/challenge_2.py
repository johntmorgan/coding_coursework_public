#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:47:21 2023

@author: johnmorgan
"""

from MinHeap import MinHeap

# O(klogn)
# O(n) to build, k * O(logn) to remove, O(klogn) dominates
# List comprhension result = 

def findKSmallest(lst, k):
    heap = MinHeap()
    heap.buildHeap(lst)
    # result = []
    # for i in range(k):
    #     result.append(heap.removeMin())
    result = [heap.removeMin() for i in range(k)]
    return result

# Optimal solution: Quick Select, O(n)

lst = [9,4,7,1,-2,6,5]
k = 3
print(findKSmallest(lst, k))