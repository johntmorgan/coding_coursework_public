#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:50:01 2023

@author: johnmorgan
"""

# O(nlogk)
# O(k) space

from point import Point
from heapq import *
from math import *

def k_closest(points, k):
    heap = []
    for index in range(0, k):
        dist = sqrt(points[index].x ** 2 + points[index].y ** 2)
        heappush(heap, (-dist, index, points[index]))
    for index in range(k, len(points)):
        dist = sqrt(points[index].x ** 2 + points[index].y ** 2)
        if -dist > heap[0][0]:
            heappop(heap)
            heappush(heap, (-dist, index, points[index]))
    return [point for _, _, point in heap]

points = [Point(-1,-3), Point(-4,-5), Point(-2,2), Point(-2,-3)]
k = 3
print(k_closest(points, k))

points = [Point(-1,-3), Point(2, -2), Point(-2,2), Point(-2,2)]
k = 3
print(k_closest(points, k))