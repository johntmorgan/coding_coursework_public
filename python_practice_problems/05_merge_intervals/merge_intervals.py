#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:39:48 2023

@author: johnmorgan
"""

from interval import *

def merge_intervals(v):
    output = [v[0]]
    for index in range(1, len(v)):
        interval = v[index]
        if interval.start <= output[len(output) - 1].end:
            if interval.end > output[len(output) - 1].end:
                output[len(output) - 1].end = interval.end
        else:
            output.append(interval)
    return output


v = [Interval(1, 5), Interval(3, 7), Interval(4, 6), Interval(8,10)]
print(merge_intervals(v))