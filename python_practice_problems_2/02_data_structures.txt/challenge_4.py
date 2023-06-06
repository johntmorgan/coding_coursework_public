#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:51:42 2023

@author: johnmorgan
"""

# Simple/slow O(n^2)

def find_product(lst):
    prod_lst = []
    for i in range(len(lst)):
        prod = 1
        for j in range(len(lst)):
            if j != i:
                prod *= lst[j]
        prod_lst += [prod]
    return prod_lst

# Only traverse twice, once in each direction O(n)

def find_product(lst):
    prod_lst = []
    left = 1
    for elem in lst:
        prod_lst.append(left)
        left = left * elem
    right = 1
    for i in range(len(lst) - 1, -1, -1):
        prod_lst[i] = prod_lst[i] * right
        right = right * lst[i]
    return prod_lst

arr = [1,2,3,4]
print(find_product(arr))