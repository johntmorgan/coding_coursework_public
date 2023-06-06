#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:53:47 2023

@author: johnmorgan
"""

from point import Point
from heapq import *
from math import *

# O(nlogk)
# Space O(k) for heap

def k_closest(points, k):
    maxh = []
    index = 0
    while k > 0:
        point = points[index]
        heappush(maxh, [-sqrt(point.x**2 + point.y**2), index, points[index]])
        index += 1
        k -= 1
    for index in range(k, len(points)):
        point = points[index]
        distance = sqrt(point.x**2 + point.y**2)
        if -distance > maxh[0][0]:
            heappop(maxh)
            heappush(maxh, [-distance, index, points[index]])
    result = []
    for elem in maxh:
        result.append(elem[2])
    return result

# k = 3
# input_arr = [[-1,-3],[-4,-5],[-2,-2],[-2,-3]]
# points = []
# for point in input_arr:
#     points.append(Point(point[0], point[1]))
# print(k_closest(points, k))

k = 3
input_arr = [[2, 2], [2, 2], [2, 2]]
points = []
for point in input_arr:
    points.append(Point(point[0], point[1]))
print(k_closest(points, k))