#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:41:20 2023

@author: johnmorgan
"""

# O(n^2)
# O(n) space
# Review - this is one of the easier ones!

def min_refuel_stops(target, start_fuel, stations):
    max_distance = [0] * (len(stations) + 1)
    max_distance[0] = start_fuel
    for index in range(len(stations)):
        dist, fuel = stations[index]
        for back_index in range(index, -1, -1):
            if max_distance[back_index] >= dist:
                new_distance = max_distance[back_index] + fuel
                next_distance = max_distance[back_index + 1]
                max_distance[back_index + 1] = max(new_distance, next_distance)
    for i in range(len(stations) + 1):
        if max_distance[i] >= target:
            return i

target = 120
start_fuel = 10
stations = [[10,60],[20,25],[30,30],[60,40]]
print(min_refuel_stops(target, start_fuel, stations))

target = 15
start_fuel = 3
stations = [[2,5],[3,1],[6,3],[12,6]]
print(min_refuel_stops(target, start_fuel, stations))