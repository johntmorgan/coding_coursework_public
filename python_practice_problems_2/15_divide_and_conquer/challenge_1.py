#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:50:17 2023

@author: johnmorgan
"""

# Brute force

def euclidean_algorithm(x, y):
    for i in range((y + 1) // 2, 0, -1):
        print(i)
        if x % i == 0 and y % i == 0:
            return i

# Divisor accumulation

def euclidean_algorithm(x, y):
    divisors = []
    curr_max = (min(x, y) + 1)// 2
    curr_val = 1
    while curr_val < curr_max:
        if x % curr_val == 0 and y % curr_val == 0:
            divisors += [curr_val]
            curr_max = curr_max / curr_val
        print(curr_val)
        curr_val += 1
    product = 1
    for divisor in divisors:
        product *= divisor
    return product

# Actual solution
# GCD does not change if larger of two replaced by difference between numbers
# Review - memorize this
# Time O(log min(x, y))

def euclidean_algorithm(x, y):
    if x == 0:
        return y
    return euclidean_algorithm(y % x, x)

x = 1071
y = 462
print(euclidean_algorithm(x, y))