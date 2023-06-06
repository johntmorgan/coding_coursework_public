#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:56:08 2023

@author: johnmorgan
"""

from heapq import *

def min_refuel_stops(target, fuel, stations): 
    if fuel > target:
        return 0
    count = 0
    heap = []
    while fuel < target:
        while stations and stations[0][0] <= fuel:
            station = stations.pop(0)
            heappush(heap, -station[1])
        if len(heap) == 0:
            return -1
        fuel += -heappop(heap)
        count += 1
    return count

target = 120
fuel = 10
stations = [[10,60],[20,25],[30,30],[60,40]]
print(min_refuel_stops(target, fuel, stations))