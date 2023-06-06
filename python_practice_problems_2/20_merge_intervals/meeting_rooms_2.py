#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:59:19 2023

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
        if h[0] <= interval.start:
            a = heapq.heappop(h)
        heapq.heappush(h, interval.end)
    return len(h)

lst = [[2,8],[3,4],[3,9],[5,11],[8,20],[11,15]]

intervals = []
for elem in lst:
    intervals.append(Interval(elem[0], elem[1]))
print(find_sets(intervals))