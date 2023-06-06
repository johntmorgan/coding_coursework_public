#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:10:08 2023

@author: johnmorgan
"""

def find_max_knapsack_profit(capacity, weights, values):
    profits = [0] * (capacity + 1)
    for i in range(len(values)):
        for c in range(capacity, -1, -1):
            if weights[i] <= c:
                new_profit = profits[c - weights[i]] + values[i]
                profits[c] = max(profits[c], new_profit)
    return profits[capacity]


capacity = 6
weights = [1,2,3,5]
values = [1,5,4,8]
print(find_max_knapsack_profit(capacity, weights, values))