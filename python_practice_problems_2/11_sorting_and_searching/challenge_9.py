#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:07:49 2023

@author: johnmorgan
"""

# O(n) but messy code and 2 loops

def dutch_national_flag(lst):
    boundary = len(lst) - 1
    c0 = 0
    for index in range(len(lst)):
        if lst[index] == 2 and index < boundary:
            lst[index], lst[boundary] = lst[boundary], lst[index]
            boundary -= 1
        if lst[index] == 0:
            c0 += 1
    start = c0
    for index in range(c0):
        if lst[index] == 1:
            swapped = False
            while not swapped and start <= boundary:
                if lst[start] == 0:
                    lst[index], lst[start] = lst[start], lst[index]
                    swapped = True
                start += 1
    return lst

# Actual solution (non-brute force)
# Review

def dutch_national_flag(lst):
    size = len(lst)
    i = 0
    mid = 0
    j = size - 1
    while mid <= j:
        if lst[mid] == 0:
            lst[i], lst[mid] = lst[mid], lst[i]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        elif lst[mid] == 1:
            mid += 1
    return lst


lst = [2, 0, 0, 1, 2, 1, 0]
print(dutch_national_flag(lst))

lst = [2, 0, 0, 1, 2, 0, 1]
print(dutch_national_flag(lst))

print(dutch_national_flag([2, 0, 0, 1, 2, 1]))