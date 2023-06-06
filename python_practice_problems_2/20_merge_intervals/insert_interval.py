#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:25:04 2023

@author: johnmorgan
"""

# Naive
# Mark each interval as non-visited
# Find overlaps and merge, then mark as visited
# Time complexity O(n^2)

# O(n) time, O(1) space

from interval import *

def insert_interval(existing_intervals, new_interval):
    result, covered = [], []
    for index in range(len(existing_intervals)):
        if existing_intervals[index].start <= new_interval.start:
            result.append(existing_intervals[index])
            covered.append(index)
    removed = []
    for index in range(len(result)):
        if result[index].end >= new_interval.start:
            # Two intervals merged
            if result[index].end < new_interval.end:
                new_interval = Interval(result[index].start, new_interval.end)
                removed.append(index)
            # New interval swallowed by single interval
            elif result[index].end >= new_interval.end:
                new_interval = None
    for index in range(len(removed) - 1, -1, -1):
        result.pop(removed[index])
    result.append(new_interval)
    for index in range(len(existing_intervals)):
        if index not in covered:
            if existing_intervals[index].start <= result[-1].end:
                if existing_intervals[index].end > result[-1].end:
                    result.append(Interval(result.pop().start, existing_intervals[index].end))
                covered.append(index)
    for index in range(len(existing_intervals)):
        if index not in covered:
            result.append(existing_intervals[index])
    return result

# Tighter course solution

def insert_interval(existing_intervals, new_interval):
    new_start, new_end = new_interval.start, new_interval.end
    i = 0
    n = len(existing_intervals)
    output = []
    while i < n and existing_intervals[i].start < new_start:
        output.append(existing_intervals[i])
        i = i + 1
    if not output or output[-1].end < new_start:
        output.append(new_interval)
    else:
        output[-1].end = max(output[-1].end, new_end)
    while i < n:
        ei = existing_intervals[i]
        start, end = ei.start, ei.end
        if output[-1].end < start:
            output.append(ei)
        else:
            output[-1].end = max(output[-1].end, end)
        i += 1
    return output

# lst = [[1,2],[3,4],[5,8],[9,15]]
# added = [2,5]
# ints = []
# for interval in lst:
#     ints.append(Interval(interval[0], interval[1]))
# added_int = Interval(added[0], added[1])
# results = insert_interval(ints, added_int)
# for result in results:
#     print(result.start, result.end)
    
lst = [[1, 6], [8, 9], [10, 15], [16, 18]]
added = [9, 10]
ints = []
for interval in lst:
    ints.append(Interval(interval[0], interval[1]))
added_int = Interval(added[0], added[1])
results = insert_interval(ints, added_int)
for result in results:
    print(result.start, result.end)

    # for r in result:
    #     print(r.start, r.end)