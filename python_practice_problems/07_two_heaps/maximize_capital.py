#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:34:13 2023

@author: johnmorgan
"""

from heapq import *
from min_heap import *
from max_heap import *

def maximum_capital(c, k, capitals, profits):
    used = []
    while k > 0:
        maxh = max_heap()
        projects = False
        for index in range(len(capitals)):
            if capitals[index] <= c and profits[index] not in used:
                maxh.insert(profits[index])
                projects = True
        if projects:
            best_project = maxh.get_max()
            c += best_project
            used.append(best_project)
            k -= 1
        else:
            k = 0
    return c

c = 1
k = 2
capitals = [1, 2, 2, 3]
profits = [2, 4, 6, 8]
print(maximum_capital(c, k, capitals, profits))