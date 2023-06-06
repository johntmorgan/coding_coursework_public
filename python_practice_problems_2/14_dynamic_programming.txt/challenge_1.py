#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:15:10 2023

@author: johnmorgan
"""

# Brute force JM solution
# O(2^n) complexity

def calculate_profit(profits, weights, capacity, total_profit):
    if len(profits) == 1:
        if capacity < 0:
            return float('-inf')
        elif capacity >= weights[0]:
            return total_profit + profits[0]
        else:
            return total_profit
    else:
        return max(calculate_profit(profits[1:], weights[1:], capacity, total_profit),
            calculate_profit(profits[1:], weights[1:], capacity - weights[0],
                             total_profit + profits[0]))

def knap_sack(profits, profits_length, weights, capacity):
    total_profit = 0
    return calculate_profit(profits, weights, capacity, total_profit)

# Brute force course solution
# O(2^n) complexity

def knap_sack_recursive(profits, profits_length, weights, capacity, current_index):
    if capacity <= 0 or current_index >= profits_length or current_index < 0:
        return 0
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + knap_sack_recursive(profits, profits_length, weights,
                                                     capacity - weights[current_index], current_index + 1)
    profit2 = knap_sack_recursive(profits, profits_length, weights, capacity, current_index + 1)
    return max(profit1, profit2)

def knap_sack(profits, profits_length, weights, capacity):
    return knap_sack_recursive(profits, profits_length, weights, capacity, 0)

# Top-down with memoization
# O(N * C) capacity

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

# Bottom up with tabularization

def knap_sack(profits, profits_length, weights, capacity):
    if capacity <= 0 or profits_length == 0:
        return 0
    lookup_table = [[0 for x in range(capacity + 1)] for x in range(profits_length + 1)]
    for i in range(profits_length + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                lookup_table[i][j] = 0
            elif weights[i - 1] <= j:
                lookup_table[i][j] = max(profits[i - 1] + lookup_table[i - 1][j - weights[i - 1]],
                                         lookup_table[i - 1][j])
            else:
                lookup_table[i][j] = lookup_table[i - 1][j]
    print(lookup_table)
    return lookup_table[profits_length][capacity]

# Tabularization, space-optimized

# def knap_sack(profits, profits_length, weights, capacity):
#     if capacity <= 0 or profits_length == 0:
#         return 0
#     lookup_table = [0 for x in range(capacity + 1)]
#     # if we have only one weight, we will take it if it is not more than the
#     # capacity
#     for i in range(capacity + 1):
#         if weights[0] <= i:
#             lookup_table[i] = profits[0]
#     for i in range(1, profits_length):
#         for j in reversed(range(capacity + 1)):
#             profit1 = 0
#             profit2 = 0
#             # include the item, if it is not more than the capacity
#             if weights[i] <= j:
#                 profit1 = profits[i] + lookup_table[j - weights[i]]
#             # exclude the item
#             profit2 = lookup_table[j]
#             # take maximum
#             lookup_table[j] = max(profit1, profit2)
#     return lookup_table[capacity]


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