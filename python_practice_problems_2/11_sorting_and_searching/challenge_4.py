#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:20:33 2023

@author: johnmorgan
"""

# O(n)

def sort_binary_list(lst):
    c0, c1 = 0, 0
    for elem in lst:
        if elem == 0:
            c0 += 1
        else:
            c1 += 1
    return [0] * c0 + [1] * c1

# Swap 1s solution
# O(n)
# Less space complexity than my answer

def sort_binary_lst(lst):
    j = 0
    for i in range(len(lst)):
        if lst[i] < 1:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst

lst = [1, 0, 1, 0, 1, 1, 0, 0]
print(sort_binary_list(lst))