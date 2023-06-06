#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:24:05 2023

@author: johnmorgan
"""

def attend_all_meetings(intervals):
    intervals.sort()
    last_time = 0
    for interval in intervals:
        if interval[0] >= last_time:
            last_time = interval[1]
        else:
            return False
    return True