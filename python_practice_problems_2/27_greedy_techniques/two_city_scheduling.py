#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:30:31 2023

@author: johnmorgan
"""

# O(nlogn) due to sort
# O(n + m) space complexity - m being memory used to sort
# Python O(m) merge/insertion combo - different in Java, C++

def two_city_scheduling(costs):
    extra = []
    for cost in costs:
        extra.append([cost[0] - cost[1], cost[0], cost[1]])
    extra.sort()
    total_cost = 0
    for index in range(0, len(costs) // 2):
        total_cost += extra[index][1]
    for index in range(len(costs) // 2, len(costs)):
        total_cost += extra[index][2]
    return total_cost

costs = [[10,20],[30,200],[400,50],[30,20]]
print(two_city_scheduling(costs))