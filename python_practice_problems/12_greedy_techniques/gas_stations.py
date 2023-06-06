#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:44:54 2023

@author: johnmorgan
"""

# Review - came up with slow solution
# O(n^2)

def gas_station_journey(gas, cost):
    if sum(cost) > sum(gas):
        return -1
    for index in range(len(gas)):
        start = index
        gas_in_tank = (gas[index] - cost[index])
        gas_ok = gas_in_tank >= 0
        index += 1
        while gas_ok and index != start:
            if index == len(gas):
                index = 0
            else:
                gas_in_tank += (gas[index] - cost[index])
                gas_ok = gas_in_tank >= 0
                index += 1
        if gas_ok:
            return start
    return -1

# There *must* be a valid starting index if sum(gas) >= sum(cost)
# So just find it, O(n)

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