#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:53:42 2023

@author: johnmorgan
"""

from interval import *

def insert_interval(existing_intervals, new_interval):
    output = []
    curr_index = 0
    merged_interval, appended = Interval(new_interval.start, new_interval.end), False
    while curr_index < len(existing_intervals):
        interval = existing_intervals[curr_index]
        if interval.end < new_interval.start:
            output.append(interval)
        elif interval.start > new_interval.end:
            output.append(interval)
        else:
            if appended:
                merged_interval = output.pop()
            if interval.start < merged_interval.start:
                merged_interval.start = interval.start
            if interval.end > merged_interval.end:
                merged_interval.end = interval.end
            output.append(merged_interval)
            appended = True
        curr_index += 1
    if not appended:
        output.append(merged_interval)
    return output
    
    
a = Interval(1, 2)
b = Interval(3, 4)
c = Interval(5, 8)
d = Interval(9, 15)
existing_intervals = [a, b, c, d]
new_interval = Interval(2, 5)
merged_intervals = insert_interval(existing_intervals, new_interval)
for interval in merged_intervals:
    print(interval)