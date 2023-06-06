#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:51:58 2023

@author: johnmorgan
"""

# Naive, nested loop O(n^2)

from interval import Interval

def intervals_intersection(A, B):
    result = []
    ind_A, ind_B = 0, 0
    while ind_A < len(A) and ind_B < len(B):
        if A[ind_A].start == B[ind_B].start:
            if A[ind_A].end <= B[ind_B].end:
                result.append(Interval(A[ind_A].start, A[ind_A].end))
                ind_A += 1
            else:
                result.append(Interval(A[ind_A].start, B[ind_B].start))
                ind_B += 1             
        elif A[ind_A].start < B[ind_B].start:
            if A[ind_A].end >= B[ind_B].start:
                if A[ind_A].end <= B[ind_B].end:
                    result.append(Interval(B[ind_B].start, A[ind_A].end))
                    ind_A += 1
                else:
                    result.append(Interval(B[ind_B].start, B[ind_B].start))
                    ind_B += 1
            else:
                ind_A += 1
        else:
            if B[ind_B].end >= A[ind_A].start:
                if B[ind_B].end <= A[ind_A].end:
                    result.append(Interval(A[ind_A].start, B[ind_B].end))
                    ind_B += 1
                else:
                    result.append(Interval([ind_A].start, A[ind_A].start))
                    ind_A += 1
            else:
                ind_B += 1
    return result

# Far better course code
# Review

def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    i = j = 0
    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i].start, interval_list_b[j].start)
        end = min(interval_list_a[i].end, interval_list_b[j].end)
        if start <= end:
            intersections.append(Interval(start, end))
        if interval_list_a[i].end < interval_list_b[j].end:
            i += 1
        else:
            j += 1

    return intersections

l1 = [[1,4],[5,6],[7,8],[9,15]]
l2 = [[2,4],[5,7],[9,15]]
l1_ints, l2_ints = [], []
for interval in l1:
    l1_ints.append(Interval(interval[0], interval[1]))
for interval in l2:
    l2_ints.append(Interval(interval[0], interval[1]))
results = intervals_intersection(l1_ints, l2_ints)
for result in results:
    print(result.start, result.end)