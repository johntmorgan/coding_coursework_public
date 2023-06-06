#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:42:34 2023

@author: johnmorgan
"""

# Brute force
# O(2^denomslength)

def count_change(denoms, denoms_length, amount):
    if amount == 0:
        return 1
    if amount < 0 or denoms_length <= 0:
        return 0
    if denoms_length <= 0 and amount >= 1:
        return 0
    return count_change(denoms, denoms_length - 1, amount) + count_change(denoms, denoms_length, amount - denoms[denoms_length - 1])

# Memoization
# O(denomslength * amount)

def count_change_recursive(denoms, denoms_length, amount, lookup_table):
    if amount == 0:
        return 1
    if amount < 0 or denoms_length == 0:
        return 0
    if lookup_table[denoms_length - 1][amount] != 0:
        return lookup_table[denoms_length - 1][amount]
    lookup_table[denoms_length - 1][amount] = count_change_recursive(denoms, denoms_length - 1, amount,
                                                                     lookup_table) + \
                                              count_change_recursive(denoms, denoms_length,
                                                                     amount - denoms[denoms_length - 1],
                                                                     lookup_table)
    return lookup_table[denoms_length - 1][amount]

# Tabularization
# O(denomslength * amount)

def count_change(denoms, denoms_length, amount):
    lookup_table = [[0 for x in range(amount + 1)] for x in range(denoms_length)]
    return count_change_recursive(denoms, denoms_length, amount, lookup_table)

def count_change(denoms, denoms_length, amount):
    if amount <= 0 or denoms_length <= 0:
        return 0
    lookup_table = [[0 for x in range(denoms_length)] for x in range(amount + 1)]
    for i in range(denoms_length):
        lookup_table[0][i] = 1
    for i in range(1, amount + 1):
        for j in range(denoms_length):
            x = lookup_table[i - denoms[j]][j] if i - denoms[j] >= 0 else 0
            y = lookup_table[i][j - 1] if j >= 1 else 0
            lookup_table[i][j] = x + y
    return lookup_table[amount][denoms_length - 1]


amount = 10 # num of cents
denoms = [25, 10, 5, 1]
denoms_length = 4
print(count_change(denoms, denoms_length, amount))