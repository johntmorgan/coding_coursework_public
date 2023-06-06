#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:26:37 2023

@author: johnmorgan
"""

# O(n^2) complexity

def find_min_coins(v, coins_available):
    result = []
    remainder = v
    coin_index = -1
    while remainder > 0:
        current_coin = coins_available[coin_index]
        while current_coin <= remainder:
            remainder -= current_coin
            result.append(current_coin)
        coin_index -= 1
    return result

# Book solution tighter code, same time complexity

def find_min_coins(v, coins_available):
    result = []
    n = len(coins_available)
    for i in reversed(range(n)):
        while v >= coins_available[i]:
            v -= coins_available[i]
            result.append(coins_available[i])
    return result

v = 19
coins_available = [1, 5, 10, 25]
print(find_min_coins(v, coins_available))