#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:44:14 2023

@author: johnmorgan
"""

from heapq import *

class max_heap:
    def __init__(self):
        self.max_heap_list = []

    def insert(self, x):
        heappush(self.max_heap_list, -x)

    def pop(self):
        return -heappop(self.max_heap_list)

    def get_max(self):
        return -self.max_heap_list[0]

    def __str__(self):
        out = "["
        for i in self.max_heap_list:
            out+=str(i) + ", "
        out = out[:-2] + "]"
        return out