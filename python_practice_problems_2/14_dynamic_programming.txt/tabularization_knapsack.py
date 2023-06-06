#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:23:43 2023

@author: johnmorgan
"""

def knap_sack(profits, profits_length, weights, capacity):
    if capacity <= 0 or profits_length == 0:
        return 0
    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
    for i in range(profits_length + 1):
        for j in range(capacity + 1):
            print(i, j)
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            elif weights[i - 1] <= j:
                lookup_table[i][j] = max(profits[i - 1] + lookup_table[i - 1][j - weights[i - 1]],
                                         lookup_table[i - 1][j])
            else:
                lookup_table[i][j] = lookup_table[i - 1][j]
            print(lookup_table)
    return lookup_table[profits_length][capacity]

profits = [60, 100, 120] 
profits_length = 3
weights = [10, 20, 30] 
capacity = 50 # knapsack weight

print(knap_sack(profits, profits_length, weights, capacity))

profits = [60, 100, 120] 
profits_length = 3
weights = [10, 20, 30] 
capacity = 10 # knapsack weight

print(knap_sack(profits, profits_length, weights, capacity))