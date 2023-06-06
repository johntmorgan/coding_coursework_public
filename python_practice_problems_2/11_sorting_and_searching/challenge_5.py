#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:27:54 2023

@author: johnmorgan
"""

# O(n)
# Actually the book solution

def find_max_prod(lst):
    pos1, pos2 = 0, 0
    neg1, neg2 = 0, 0
    for elem in lst:
        if elem > pos1:
            if elem > pos2:
                pos1, pos2 = pos2, elem
            else:
                pos1 = elem
        if elem < neg2:
            if elem < neg1:
                neg1, neg2 = elem, neg1
            else:
                neg2 = elem
    if neg1 * neg2 > pos1 * pos2:
        return neg1, neg2
    return pos1, pos2


lst = [1, 3, 5, 2, 6]
print(find_max_prod(lst))
