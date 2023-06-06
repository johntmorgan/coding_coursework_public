#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:06:47 2023

@author: johnmorgan
"""

from interval import *

# O(n) time
# O(1) space

def merge_intervals(v):
    result = []
    for interval in v:
        if result == []:
            result.append(interval)
        else:
            if result[-1].end >= interval.start:
                if interval.end > result[-1].end:
                    result[-1].end = interval.end
            else:
                result.append(interval)
    return result

lst = [[1,5],[3,7],[4,6]]
ints = []
for interval in lst:
    ints.append(Interval(interval[0], interval[1]))
results = merge_intervals(ints)
for result in results:
    print(result.start, result.end)
    
lst = [[1,5],[4,6],[6,8],[11,15]]
ints = []
for interval in lst:
    ints.append(Interval(interval[0], interval[1]))
results = merge_intervals(ints)
for result in results:
    print(result.start, result.end)