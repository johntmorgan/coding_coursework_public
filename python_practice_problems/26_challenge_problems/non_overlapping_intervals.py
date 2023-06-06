#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 17:18:38 2023

@author: johnmorgan
"""

def remove_minimum_intervals(intervals):
    intervals.sort()
    removed = 0
    curr_time = 0
    for interval in intervals:
        if interval[0] < curr_time:
            removed += 1
        else:
            curr_time = interval[1]
    return removed
    
    
intervals = [[1,2],[2,4],[3,6],[5,10]]
print(remove_minimum_intervals(intervals))