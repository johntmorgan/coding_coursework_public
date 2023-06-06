#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:09:02 2023

@author: johnmorgan
"""

class graph:
    def __init__(self):
        self.graph = {}
        
    def initialize_graph(self, dependencies):
        for x in dependencies:
            parent, child = x[1], x[0]
            self.graph[parent], self.graph[child] = [], []
            
    def build_graph(self, dependencies):
        for x in dependencies:
            parent, child = x[1], x[0]
            self.graph[parent].append(child)
            
def can_finish(n, prereqs):
    dgraph = graph()
    dgraph.initialize_graph(prereqs)
    dgraph.build_graph(prereqs)
    indegrees = {}
    for node in dgraph.graph:
        if node not in indegrees:
            indegrees[node] = 0
        for child in dgraph.graph[node]:
            if child not in indegrees:
                indegrees[child] = 1
            else:
                indegrees[child] += 1
    sources = []
    for node in indegrees:
        if indegrees[node] == 0:
            sources.append(node)
            indegrees[node] = -1
    while sources:
        node = sources.pop(0)
        for child in dgraph.graph[node]:
            if indegrees[child] == 1:
                sources.append(child)
                indegrees[child] = -1
            elif indegrees[child] > 1:
                indegrees[child] -= 1
            else:
                return False
    for node in indegrees:
        if indegrees[node] != -1:
            return False
    return True
    
    
    
n = 2
prereqs = [[1,0],[0,1]]
print(can_finish(n, prereqs))

n = 5
prereqs = [[1,0],[2,1],[3,2],[4,3]]
print(can_finish(n, prereqs))

n = 8
prereqs = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 2], [1, 6], [7, 1]]
print(can_finish(n, prereqs))