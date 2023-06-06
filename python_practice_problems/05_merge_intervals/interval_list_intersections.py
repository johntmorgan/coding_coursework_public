#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:16:58 2023

@author: johnmorgan
"""

# O(n + m)

from interval import Interval

def intervals_intersection(A, B):
    output = []
    a, b = 0, 0
    while a < len(A) and b < len(B):
        if A[a].end < B[b].end:
            if A[a].start >= B[b].start:
                output.append(A[a])
            elif B[b].start <= A[a].end:
                output.append(Interval(B[b].start, A[a].end))
            a += 1
        elif B[b].end < A[a].end:
            if B[b].start >= A[a].start:
                output.append(B[b])
            elif A[a].start <= B[b].end:
                output.append(Interval(A[a].start, B[b].end))
            b += 1  
        else:
            if B[b].start >= A[a].start:
                output.append(B[b])
            else:
                output.append(Interval(A[a].start, B[b].end))
            a += 1
            b += 1
    return output

# A = [Interval(1,3),Interval(5,6),Interval(7,8),Interval(9,15)]
# B = [Interval(2,4),Interval(5,7),Interval(9,15)]
# merged_intervals = intervals_intersection(A, B)
# for interval in merged_intervals:
#     print(interval)
    
A = [Interval(1,4),Interval(5,6),Interval(7,8),Interval(9,15)]
B = [Interval(2,4),Interval(5,7),Interval(9,15)]
merged_intervals = intervals_intersection(A, B)
for interval in merged_intervals:
    print(interval)