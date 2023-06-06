#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:30:01 2023

@author: johnmorgan
"""

# O(m + n) again

def is_disjoint(list1, list2):
    dset = set()
    for elem in list1:
        dset.add(elem)
    for elem2 in list2:
        if elem2 in dset:
            return False
    return True


list1 = [9,4,3,1,-2,6,5]
list2 = [7, 8, 10]
list3 = [7, 8, 3]

print(is_disjoint(list1, list2))
print(is_disjoint(list1, list3))