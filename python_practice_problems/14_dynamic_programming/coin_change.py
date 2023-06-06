#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:20:51 2023

@author: johnmorgan
"""

# Review
# Provided answer
# O(n * m) - n is total and number of subproblems, m coins

def recurse_coin_change(coins, rem, counter):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    # If you already know min to get to remaining, just use
    if counter[rem] != float('inf'):
        return counter[rem]
    minimum = float('inf')
    for coin in coins:
        result = recurse_coin_change(coins, rem - coin, counter)
        if result > -1:
            minimum = result + 1
    if minimum == float('inf'):
        counter[rem] = float('inf')
        return -1
    else:
        counter[rem] = minimum
    return counter[rem]

def coin_change(coins, total):
    if total <= 0:
        return 0
    counter = [0] + [float('inf')] * total
    return recurse_coin_change(coins, total, counter)

# without offset

def recurse_coin_change(coins, rem, counter):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    # If you already know min to get to remaining, just use
    if counter[rem] != float('inf'):
        return counter[rem]
    minimum = float('inf')
    for coin in coins:
        result = recurse_coin_change(coins, rem - coin, counter)
        if result > -1:
            minimum = result + 1
    if minimum == float('inf'):
        counter[rem] = float('inf')
        return -1
    else:
        counter[rem] = minimum
    return counter[rem]

def coin_change(coins, total):
    if total <= 0:
        return 0
    counter = [0] + [float('inf')] * total
    return recurse_coin_change(coins, total, counter)

# # No table works, but is exponential k^n where k = # coins, n = total

# def recurse_coin_change(coins, rem):
#     if rem < 0:
#         return -1
#     if rem == 0:
#         return 0
#     minimum = float('inf')
#     for coin in coins:
#         result = recurse_coin_change(coins, rem - coin)
#         if result > -1:
#             minimum = result + 1
#     if minimum == float('inf'):
#         return -1
#     else:
#         return minimum

# def coin_change(coins, total):
#     if total <= 0:
#         return 0
#     return recurse_coin_change(coins, total)

    
coins = [1,2,5]
total = 11
print(coin_change(coins, total)) 