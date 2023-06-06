#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:25:51 2023

@author: johnmorgan
"""

# O(n)

def find_second_maximum(lst):
    biggest, second_biggest = float('-inf'), float('-inf')
    for elem in lst:
        if elem > biggest:
            second_biggest = biggest
            biggest = elem
        elif elem > second_biggest:
            second_biggest = elem
    if second_biggest == float('-inf'):
        return None
    else:
        return second_biggest

# Can also traverse list twice
# Find max, then find second max
# Also O(n)

# Can also sort and return second to last element, lst[-2]
# However O(nlogn) and second to last element may be a duplicate

max_list = [9,2,3,6]
print(find_second_maximum(max_list))