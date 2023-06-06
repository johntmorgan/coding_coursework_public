#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:53:41 2023

@author: johnmorgan
"""

from MaxHeap import MaxHeap

# O(klogn) again

def findKLargest(lst, k):
    heap = MaxHeap()
    heap.buildHeap(lst)
    return [heap.removeMax() for i in range(k)]

# Once again, Quick Select optimal
# Also good for finding kth value in list - set k, pick last value!

lst = [9,4,7,1,-2,6,5]
k = 3
print(findKLargest(lst, k))