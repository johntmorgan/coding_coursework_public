#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:41:20 2023

@author: johnmorgan
"""

from heapq import *
from min_heap import *
from max_heap import *

# Naive
# Traverse and create array of viable projects
# O(n^2) - traverse every time
# O(n) space complexity, new array

# O(nlogn)
# O(n) space complexity still, to store

def maximum_capital(c, k, capitals, profits):
    spent_projects = []
    while k > 0:
        maxh = max_heap()
        for index in range(len(capitals)):
            if capitals[index] <= c and profits[index] not in spent_projects:
                maxh.insert(profits[index])
        if len(maxh.max_heap_list) > 0:
            project_profit = maxh.get_max()
            c += project_profit
            spent_projects.append(project_profit)
            k -= 1
        else:
            return c
    return c

# Course colution

def maximum_capital(c, k, capitals, profits):
    current_capital = c
    capitals_min_heap = []
    profits_max_heap = []
    for x in range(0, len(capitals)):
        heappush(capitals_min_heap, (capitals[x], x))
    for _ in range(k):
        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            c, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[i], i))
        if not profits_max_heap:
            break
        j = -heappop(profits_max_heap)[0]
        current_capital = current_capital + j
    return current_capital

c = 1
k = 2
capitals = [1,2,2,3]
profits = [2,4,6,8]
print(maximum_capital(c, k, capitals, profits))

c = 1
k = 3
capitals = [0,1,2] 
profits = [1,2,3]
print(maximum_capital(c, k, capitals, profits))