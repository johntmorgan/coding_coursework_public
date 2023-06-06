#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:04:39 2023

@author: johnmorgan
"""

# Naive - count equal to boat limit
# Then loop through again to pair
# O(n^2)

# O(n + nlogn) -> O(nlogn)
# Space O(n) due to sort in Python
    
def rescue_boats(people, limit):
    people.sort()
    boats = 0
    light = 0
    heavy = len(people) - 1
    while light < heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
        else:
            heavy -= 1
        boats += 1
    if light == heavy:
        boats += 1
    return boats

people = [3,1,4,2,4]
limit = 4
print(rescue_boats(people, limit))