#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:05:31 2023

@author: johnmorgan
"""

# O(nlogn) because sort
# O(n) because sort

def rescue_boats(people, limit):
    people.sort()
    low, high = 0, len(people) - 1
    boats = 0
    while low <= high:
        if people[low] + people[high] <= limit:
            low += 1
        boats += 1
        high -= 1
    return boats

    
people = [3,1,4,2,4]
limit = 4
print(rescue_boats(people, limit))