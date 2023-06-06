#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:10:53 2023

@author: johnmorgan
"""

from graph import *
from collections import deque

# All test cases running fine on machine - not Educative? Huh.
# O(V + E)
# O(V) space

def find_compilation_order(dependencies):
    dgraph = graph()
    dgraph.initializing_graph(dependencies)
    dgraph.building_graph(dependencies)
    dgraph.graph_list
    indegrees = {}
    for key, value in dgraph.graph_list.items():
        if key not in indegrees:
            indegrees[key] = 0
        for child in value:
            if child not in indegrees:
                indegrees[child] = 1
            else:
                indegrees[child] = indegrees[child] + 1
    sources = deque()
    for key, val in indegrees.items():
        if val == 0:
            sources.append(key)
    order = []
    while len(sources) > 0:
        visit = sources.popleft()
        order += [visit]
        children = dgraph.graph_list[visit]
        for child in children:
            indegrees[child] = indegrees[child] - 1
            if indegrees[child] == 0:
                sources.append(child)
    return order

dependencies = [["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]
print(find_compilation_order(dependencies))

dependencies = [["B","A"],["C","A"],["D","B"],["E","B"],["E","D"],["E","C"],["F","D"],["F","E"],["F","C"]]
print(find_compilation_order(dependencies))

dependencies = [["A","B"],["B","A"]]
print(find_compilation_order(dependencies))

dependencies = [["B","C"],["C","A"],["A","F"]]
print(find_compilation_order(dependencies))

dependencies = [["C","C"]]
print(find_compilation_order(dependencies))