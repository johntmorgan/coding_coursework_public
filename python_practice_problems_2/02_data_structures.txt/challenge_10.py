#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 17:08:13 2023

@author: johnmorgan
"""

# O(n)

def max_min(lst):
    mm_list = []
    if len(lst) > 0:
        left, right = 0, len(lst) - 1
        while left != right:
            mm_list += [lst[right]]
            right -= 1
            if left != right:
                mm_list += [lst[left]]
                left += 1
        mm_list += [lst[left]]
    return(mm_list)

# O(n) using O(1) space

def max_min(lst):
    if len(lst) == 0:
        return []
    left, right = 0, len(lst) - 1
    max_elem = lst[-1] + 1
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] += (lst[right] % max_elem) * max_elem
            right -= 1
        else:
            lst[i] += (lst[left] % max_elem) * max_elem
            left += 1
    for i in range(len(lst)):
        lst[i] = lst[i] // max_elem
    return lst

lst = [1,2,3,4,5,6,7]
print(max_min(lst))
lst = [1,2,3,4,5,6]
print(max_min(lst))