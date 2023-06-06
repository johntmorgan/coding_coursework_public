#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:12:07 2023

@author: johnmorgan
"""

from decimal import Decimal  # Decimal library to assign minimum/maximum numbers

# Brute force

def egg_drop(eggs, floors):
    if eggs <= 0:
        return 0
    if floors == 1 or floors == 0:
        return floors
    if eggs == 1:
        return floors
    min = Decimal("Infinity")
    res = 0
    for i in range(1, floors + 1):
        res = max(egg_drop(eggs - 1, i - 1), egg_drop(eggs, floors - i))
        if res < min:
            min = res
    return min + 1

# Memoization

def egg_drop_recursive(eggs, floors, lookup_table):
    if eggs <= 0:
        return 0
    if floors == 1 or floors == 0:
        return floors
    if eggs == 1:
        return floors
    if lookup_table[eggs][floors] != Decimal("Infinity"):
        return lookup_table[eggs][floors]
    for i in range(1, floors + 1):
        res = 1 + max(egg_drop_recursive(eggs - 1, i - 1, lookup_table),
                        egg_drop_recursive(eggs, floors - i, lookup_table))

        if res < lookup_table[eggs][floors]:
            lookup_table[eggs][floors] = res

    return lookup_table[eggs][floors]

def egg_drop(eggs, floors):
    lookup_table = [[Decimal("Infinity") for i in range(floors + 1)] for i in range(eggs + 1)]
    return egg_drop_recursive(eggs, floors, lookup_table)

# Tabularization
# O((eggs * floors)^2)

def egg_drop(eggs, floors):
    if eggs <= 0:
        return 0
    if floors == 1 or floors == 0:
        return floors
    if eggs == 1:
        return floors
    egg_floor = [[0 for i in range(floors + 1)] for i in range(eggs + 1)]
    res = 0
    for i in range(1, eggs + 1):
        egg_floor[i][1] = 1
        egg_floor[i][0] = 0
    for j in range(1, floors + 1):
        egg_floor[1][j] = j
    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            egg_floor[i][j] = Decimal("Infinity")

            for x in range(1, j + 1):
                res = 1 + max(egg_floor[i - 1][x - 1], egg_floor[i][j - x])
                if (res < egg_floor[i][j]):
                    egg_floor[i][j] = res
    return egg_floor[eggs][floors]

# Optimal for interview
# O(eggs∗log(floors))

def binomial_coeff(x, n, k):
    sum = 0
    term = 1
    for i in range(1, n + 1):
        if sum < k:
            term *= x - i + 1
            term //= i
            sum += term
    return sum

def egg_drop(eggs, floors):
    if eggs <= 0:
        return 0
    if floors == 1 or floors == 0:
        return floors
    if eggs == 1:
        return floors
    low = 1
    high = floors
    while low < high:
        mid = (low + high) // 2
        if binomial_coeff(mid, eggs, floors) < floors:
            low = mid + 1
        else:
            high = mid
    return low

eggs = 6
floors = 15