#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:11:54 2023

@author: johnmorgan
"""

# O(n^2)

def gas_station_journey(gas, cost):
    gas_sum, cost_sum = 0, 0
    for index in range(len(gas)):
        gas_sum += gas[index]
        cost_sum += cost[index]
    if gas_sum < cost_sum:
        return -1
    for i in range(len(gas)):
        gas_tank = 0
        loc, target, failed = i, -1, False
        while loc != target and failed == False:
            if gas[loc] + gas_tank >= cost[loc]:
                gas_tank = gas_tank + gas[loc] - cost[loc]
                if loc < len(gas) - 1:
                    loc += 1
                else:
                    loc = 0
            else:
                failed = True
            if target == -1:
                if loc > 0:
                    target = loc - 1
                else:
                    target = len(gas) - 1
        if failed == False:
            return i
    return -1

# O(n) course solution, review

def gas_station_journey(gas, cost):
    if sum(cost) > sum(gas):
        return -1
    total_gas, starting_index = 0, 0
    for i in range(len(gas)):  
        total_gas = total_gas + (gas[i] - cost[i])
        if total_gas < 0:
            total_gas = 0
            starting_index = i + 1
    return starting_index

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(gas_station_journey(gas, cost))

gas = [1, 1, 1, 1, 10] 
cost = [2, 2, 1, 3, 1]
print(gas_station_journey(gas, cost))