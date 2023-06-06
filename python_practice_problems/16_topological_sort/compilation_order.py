#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:19:48 2023

@author: johnmorgan
"""

# O(V + E) time
# O(V) space

from graph import *
from collections import deque

def find_compilation_order(dependencies):
    dgraph = graph()
    dgraph.initializing_graph(dependencies)
    dgraph.building_graph(dependencies)
    indegrees = {}
    for parent in dgraph.graph:
        if parent not in indegrees:
            indegrees[parent] = 0
        for child in dgraph.graph[parent]:
            if child in indegrees:
                indegrees[child] += 1
            else:
                indegrees[child] = 1
    sources = deque()
    for node in indegrees:
        if indegrees[node] == 0:
            sources.append(node)
            indegrees[node] = -1
    result = []
    while sources:
        node = sources.popleft()
        result.append(node)
        if node in dgraph.graph:
            for child in dgraph.graph[node]:
                indegrees[child] -= 1
        for node in indegrees:
            if indegrees[node] == 0:
                sources.append(node)
                indegrees[node] = -1
    # Check for cycle
    if len(result) != len(indegrees):
        return []
    return result
        


dependencies = [["B","A"],["C","A"],["D","C"],["E","D"],["E","B"]]    
print(find_compilation_order(dependencies))

