#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:57:57 2023

@author: johnmorgan
"""

def search_insert_position(lst, value):
    first = 0
    last = len(lst) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            first = mid + 1
        else:
            last = mid - 1
    if lst[mid] < value:
        return mid + 1
    return mid


lst = [1, 3, 5, 6]
value = 5
print(search_insert_position(lst, value))
value = 4
print(search_insert_position(lst, value))
value = 2
print(search_insert_position(lst, value))
value = 7
print(search_insert_position(lst, value))