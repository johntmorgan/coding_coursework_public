#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:25:59 2023

@author: johnmorgan
"""

# O(n + m) complexity

def is_subset(list1, list2):
    lset = set()
    for elem in list1:
        lset.add(elem)
    for elem2 in list2:
        if elem2 not in lset:
            return False
    return True
        

list1 = [9,4,7,1,-2,6,5]
list2 = [7, 1, -2]
list3 = [7, 1, 10]

print(is_subset(list1, list2))
print(is_subset(list1, list3))