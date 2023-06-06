#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:42:56 2023

@author: johnmorgan
"""

def find_in(lst, number):
    first = 0
    last = len(lst) - 1
    list_found = False
    while first <= last and not list_found:
        mid = (first + last) // 2
        if number == lst[mid][len(lst[0]) - 1]:
            return True
        if number < lst[mid][len(lst[0]) - 1]:
            if number == lst[mid][0]:
                return True
            elif number > lst[mid][0]:
                list_found = True
            else:
                last = mid - 1
        else:
            first = mid + 1
    return binary_search(lst[mid], number)

def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False
    
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == item:
            return True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

lst  =[[10, 11, 12, 13],
       [14, 15, 16, 17],
       [27, 29, 30, 31],
       [32, 33, 39, 50]]
num = 30
print(find_in(lst, num))
num = 34
print(find_in(lst, num))