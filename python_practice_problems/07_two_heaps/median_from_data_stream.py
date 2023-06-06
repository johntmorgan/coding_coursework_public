#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:53:55 2023

@author: johnmorgan
"""

from min_heap import *
from max_heap import *

# O(nlogn) due to heapify process

# Tip: You may use some of the code templates provided
# in the support files

class MedianOfStream:
    def __init__(self):
        self.small_heap = max_heap()
        self.large_heap = min_heap()
        self.small_heap_size = 0
        self.large_heap_size = 0
  
    # This function should take a number and store it
    def insert_num(self, num):
        if self.large_heap_size == 0:
            self.large_heap.insert(num)
            self.large_heap_size += 1
        elif self.small_heap_size == 0:
            if num > self.large_heap.get_min():
                small = self.large_heap.pop()
                self.large_heap.insert(num)
                self.small_heap.insert(small)
            else:
                self.small_heap.insert(num)
            self.small_heap_size += 1
        else:
            if num < self.small_heap.get_max():
                self.small_heap.insert(num)
                self.small_heap_size += 1
            else:
                self.large_heap.insert(num)
                self.large_heap_size += 1
        while self.small_heap_size > self.large_heap_size:
            big = self.small_heap.pop()
            self.large_heap.insert(big)
            self.large_heap_size += 1
            self.small_heap_size -= 1
        while self.large_heap_size > self.small_heap_size + 1:
            small = self.large_heap.pop()
            self.small_heap.insert(small)
            self.small_heap_size += 1
            self.large_heap_size -= 1
               
    # This function should return the median of the stored numbers
    def find_median(self):
        if self.small_heap_size == self.large_heap_size:
            return (self.small_heap.get_max() + self.large_heap.get_min()) / 2.0
        else:
            return float(self.large_heap.get_min())
        
# ms = MedianOfStream()
# ms.insert_num(2)
# print(ms.find_median())
# ms.insert_num(3)
# print(ms.find_median())
# ms.insert_num(4)
# print(ms.find_median())

ms = MedianOfStream()
ms.insert_num(1)
print(ms.find_median())
ms.insert_num(-22)
print(ms.find_median())
ms.insert_num(-3)
print(ms.find_median())
ms.insert_num(-4)
print(ms.find_median())
ms.insert_num(-5)
print(ms.find_median())