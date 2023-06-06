#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:07:40 2023

@author: johnmorgan
"""

# O(n) simple JM solution

def find_peak(lst):
    for index in range(len(lst)):
        if index == 0 and lst[0] >= lst[1]:
            return lst[0]
        elif index == len(lst) - 1 and lst[len(lst) - 2] <= lst[len(lst) - 1]:
            return lst[len(lst) - 1]
        else:
            if lst[index - 1] <= lst[index] and lst[index + 1] <= lst[index]:
                return lst[index]
    return None

# O(log(n)) cutting in half every time

def find_peak_recursive(low, high, lst):
    middle = (low + high) // 2
    if middle == len(lst) - 1:
        return middle
    if lst[middle + 1] <= lst[middle] and (middle == 0 or lst[middle - 1] <= lst[middle]):
        return middle
    elif (lst[middle - 1] > lst[middle]) and middle > 0:
        return find_peak_recursive(low, middle - 1, lst)
    else:
        return find_peak_recursive(middle + 1, high, lst)

def find_peak(lst):
    return lst[find_peak_recursive(0, len(lst) - 1, lst)]

lst = [47, 85, 85, 35, 49, 49]
print(find_peak(lst))