#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 15:37:09 2023

@author: johnmorgan
"""

# O(n)

def find_symmetric(list1):
    s = set()
    symm_list = []
    for elem in list1:
        if (elem[1], elem[0]) not in s:
            s.add((elem[0], elem[1]))
        else:
            symm_list.append(elem)
            symm_list.append([elem[1], elem[0]])
    return symm_list
    
list1 = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
print(find_symmetric(list1))