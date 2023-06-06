#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:40:34 2023

@author: johnmorgan
"""

from interval import Interval
import heapq

def find_sets(intervals):
    h = []
    intervals.sort(key=lambda x: x.start)
    heapq.heappush(h, intervals[0].end)
    for index in range(1, len(intervals)):
        interval = intervals[index]
        if interval.start >= h[0]:
            heapq.heappop(h)
        heapq.heappush(h, interval.end)
    return len(h)
        
intervals = [Interval(2,8),Interval(3,4),Interval(3,9),Interval(5,11),
             Interval(8,20),Interval(11,15)]
print(find_sets(intervals))