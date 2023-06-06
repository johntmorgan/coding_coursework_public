#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:33:27 2023

@author: johnmorgan
"""

# O(k)

def right_rotate(lst, k):
    if len(lst) > 0:
        while k > 0:
            lst = [lst[-1]] + lst[:-1]
            k -= 1
        return lst
    else:
        return([])
    

def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


lst = [10,20,30,40,50]
k = 3
print(right_rotate(lst, k))
print(right_rotate([1, 2, 3, 4, 5], 2))