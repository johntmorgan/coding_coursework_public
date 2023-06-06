#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:22:01 2023

@author: johnmorgan
"""

from interval import Interval

def attend_all_meetings(intervals):
    intervals.sort()
    last_end = 0
    for interval in intervals:
        if interval[0] >= last_end:
            last_end = interval[1]
        else:
            return False
    return True

intervals = [[2,5],[1,5],[2,8],[7,9],[11,12]]
# intervals = []
# for pair in pairs:
#     intervals.append(Interval(pair[0], pair[1]))
print(attend_all_meetings(intervals))