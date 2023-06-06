#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 11:51:28 2023

@author: johnmorgan
"""

# O(n)

def findSum(lst, k):
    d = dict()
    for elem in lst:
        if elem in d.keys():
            result = [elem, k - elem]
            result.sort()
            return result
        else:
            d[k - elem] = elem
    return "No sum found"

# O(n) set version

def findSum(lst, k):
    s = set()
    for elem in lst:
        if elem in s:
            return [elem, k - elem]
        else:
            s.add(k - elem)

lst = [1,21,3,14,5,60,7,6]
k = 81
print(findSum(lst, k))