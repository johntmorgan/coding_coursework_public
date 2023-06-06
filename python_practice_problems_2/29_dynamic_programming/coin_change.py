#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 17:12:18 2023

@author: johnmorgan
"""

# O (n * m) time complexity, where n is total and m is number of coins
# O(n) space complexity, where n is total
# Review + redo, had to look at solution

def recurse_min_coins(coins, rem, counter):
    if rem < 0:
        return -1
    if rem == 0:
        return 0
    if counter[rem - 1] != float('inf'):
        return counter[rem - 1]
    
    minimum = float('inf')
    for s in coins:
        result = recurse_min_coins(coins, rem - s, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result
            
    counter[rem - 1] = minimum if minimum != float('inf') else -1
    return counter[rem - 1]

def coin_change(coins, total): 
    if total < 1:
        return 0
    counter = [float('inf')] * total
    return recurse_min_coins(coins, total, counter)

coins = [1, 2, 5]
total = 11
print(coin_change(coins, total))