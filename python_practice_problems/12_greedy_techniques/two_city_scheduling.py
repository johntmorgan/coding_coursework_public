#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:37:08 2023

@author: johnmorgan
"""

def two_city_scheduling(costs):
    cost_diff = []
    for cost in costs:
        cost_diff.append((cost[0] - cost[1], cost[0], cost[1]))
    cost_diff.sort()
    costs = 0
    for i in range(len(cost_diff) // 2):
        costs += cost_diff[i][1]
    for i in range(len(cost_diff) // 2, len(cost_diff)):
        costs += cost_diff[i][2]
    return costs
    
costs = [[10,20],[30,200],[400,50],[30,20]]
print(two_city_scheduling(costs))