#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:23:45 2023

@author: johnmorgan
"""

# O(n) time
# Kadane's algorithm, dynamic programming approach
# Written slightly differently tho - JM

def find_max_sum_sublist(lst):
    if len(lst) < 1:
        return 0
    max_sum = -float('inf')
    prior_sum = -float('inf')
    for elem in lst:
        if elem > prior_sum:
            prior_sum = elem
        else:
            prior_sum += elem
        if elem > max_sum:
            max_sum = elem
        if elem + prior_sum > max_sum:
            max_sum = elem + prior_sum
    return max_sum



lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print(find_max_sum_sublist(lst))