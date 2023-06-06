#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:12:07 2023

@author: johnmorgan
"""

from heapq import *

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.min_heap = []
        self.size = k
        for num in nums:
            heappush(self.min_heap, num)
        while len(self.min_heap) > self.size:
            heappop(self.min_heap)

    # adds element in the heap
    def add(self, val):
        if val > self.min_heap[0]:
            heappush(self.min_heap, val)
            heappop(self.min_heap)
        return self.return_Kth_largest()

    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.min_heap[0]

nums = [4,5,8,2]
k = 3

kl = KthLargest(k, nums)
print(kl.add(3))
print(kl.add(5))
print(kl.add(10))
print(kl.add(9))
print(kl.add(4))
print(kl.return_Kth_largest())