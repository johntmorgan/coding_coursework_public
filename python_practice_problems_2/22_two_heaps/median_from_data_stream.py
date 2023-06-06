#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:42:48 2023

@author: johnmorgan
"""

from min_heap import *
from max_heap import *

# Tip: You may use some of the code templates provided
# in the support files

class MedianOfStream:

    maxh= []
    minh = []
    
    def insert_num(self, num):
        if not self.maxh or -self.maxh[0] >= num:
            heappush(self.maxh, -num)
        else:
            heappush(self.minh, num)
        if len(self.maxh) > len(self.minh) + 1:
            heappush(self.minh, -heappop(self.maxh))
        elif len(self.maxh) < len(self.minh):
            heappush(self.maxh, -heappop(self.minh))
    
    def find_median(self):
        if len(self.maxh) == len(self.minh):
    
            # we have even number of elements, take the average of middle two elements
            # we divide both numbers by 2.0 to ensure we add two floating point numbers
            return -self.maxh[0] / 2.0 + self.minh[0] / 2.0
    
        # because max-heap will have one more element than the min-heap
        return -self.maxh[0] / 1.0    

["MedianOfStream","insert_num","insert_num","find_median","insert_num","find_median"]

[[],[1],[2],[],[3],[]]