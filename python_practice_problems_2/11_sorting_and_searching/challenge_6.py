#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:35:43 2023

@author: johnmorgan
"""

# Set

def find_duplicates(lst):
    s = set()
    dupe_set = set()
    dupes = []
    for elem in lst:
        if elem in s and elem not in dupe_set:
            dupes += [elem]
            dupe_set.add(elem)
        elif elem not in s:
            s.add(elem)
    return dupes

# Dict

def find_duplicates(lst):
    d = dict()
    dupes = []
    for elem in lst:
        if elem in d:
            if d[elem] == 1:
                dupes += [elem]
                d[elem] = d[elem] + 1
            else:
                d[elem] = d[elem] + 1
        else:
            d[elem] = 1
    return dupes
    

lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
print(find_duplicates(lst))