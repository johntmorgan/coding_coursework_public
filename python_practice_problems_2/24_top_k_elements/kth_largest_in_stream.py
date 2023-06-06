#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:02:16 2023

@author: johnmorgan
"""

import heapq 

# Naive
# Sort and then find elem
# (Example uses insertion sort, but why not use merge and get O(nlogn) - JM)

# O(nlogn)
# O(n) space

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.minh = []
        self.k = k
        for elem in nums:
            heapq.heappush(self.minh, elem)
        while len(self.minh) > self.k:
            heapq.heappop(self.minh)

    # adds element in the heap
    def add(self, val):
        heapq.heappush(self.minh, val)
        while len(self.minh) > self.k:
            heapq.heappop(self.minh)
        return self.return_Kth_largest()
        
    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.minh[0]
    
    
[[3,],[3],[5],[10],[9],[4]]
nums = [4,5,8,2]
k = 3
kl = KthLargest(k, nums)
print(kl.add(3))
print(kl.add(5))
print(kl.add(10))
print(kl.add(9))
print(kl.add(4))