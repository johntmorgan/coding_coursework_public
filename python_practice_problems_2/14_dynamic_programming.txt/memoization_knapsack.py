#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:36:50 2023

@author: johnmorgan
"""

def knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, current_index):
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0
    if lookup_table[current_index][capacity] != 0:
        return lookup_table[current_index][capacity]
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(lookup_table, profits,
                                                               profits_length, weights,
                                                               capacity - weights[current_index],
                                                               current_index + 1)
    profit2 = knap_sack_recursive(lookup_table, profits, profits_length,
                                  weights, capacity, current_index + 1)

    lookup_table[current_index][capacity] = max(profit1, profit2)
    return lookup_table[current_index][capacity]

def knap_sack(profits, profits_length, weights, capacity):
    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
    return knap_sack_recursive(lookup_table, profits, profits_length, weights, capacity, 0)

# Modify JM brute force

def calculate_profit(lookup_table, profits, profits_length, weights, capacity, current_index):
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0
    # Problem already solved, return solution
    if lookup_table[current_index][capacity] != 0:
        return lookup_table[current_index][capacity]
    profit_1 = 0
    if weights[current_index] <= capacity:
        profit_1 = profits[current_index] + calculate_profit(lookup_table,
                                                            profits,
                                                            profits_length,
                                                            weights,
                                                            capacity - weights[current_index],
                                                            current_index + 1)
    profit_2 = calculate_profit(lookup_table, profits, profits_length, weights,
                                capacity, current_index + 1)
    lookup_table[current_index][capacity] = max(profit_1, profit_2)
    return lookup_table[current_index][capacity]

def knap_sack(profits, profits_length, weights, capacity):
    lookup_table = [[0 for _ in range(capacity + 1)] for _ in range(profits_length + 1)]
    return calculate_profit(lookup_table, profits, profits_length, weights, capacity, 0)

profits = [60, 100, 120] 
profits_length = 3
weights = [10, 20, 30] 
capacity = 50 # knapsack weight

print(knap_sack(profits, profits_length, weights, capacity))