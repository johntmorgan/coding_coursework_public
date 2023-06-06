#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:51:52 2023

@author: johnmorgan
"""

# O(n)

def findFirstUnique(lst):
    d = dict()
    for elem in lst:
        if elem in d:
            d[elem] = d[elem] + 1
        else:
            d[elem] = 1
    for elem in lst:
        if d[elem] == 1:
            return elem
    return "No unique element in list"

# O(n), but only iterate over list once
# Using ordered collections

# import collections

# def findFirstUnique(lst):
#     orderedCounts = collections.OrderedDict()  # Creating an ordered dictionary
#     # Initializing dictionary with pairs like (lst[i],0)
#     orderedCounts = orderedCounts.fromkeys(lst, 0)
#     for ele in lst:
#         orderedCounts[ele] += 1  # Incrementing for every repitition
#     for ele in orderedCounts:
#         if orderedCounts[ele] == 1:
#             return ele
#     return None

lst = [9,2,3,2,6,6]
print(findFirstUnique(lst))