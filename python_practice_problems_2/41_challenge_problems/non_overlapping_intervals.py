#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:14:51 2023

@author: johnmorgan
"""

def remove_minimum_intervals(intervals):
    intervals.sort()
    removed = 0
    last_used = 0
    for interval in intervals:
        start, end = interval[0], interval[1]
        if start >= last_used:
            last_used = end
        else:
            removed += 1
    return removed

intervals = [[1,2],[2,4],[3,6],[5,10]]
print(remove_minimum_intervals(intervals))