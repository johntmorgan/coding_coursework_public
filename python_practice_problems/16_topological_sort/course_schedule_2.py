#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:48:14 2023

@author: johnmorgan
"""

class graph:
    def __init__(self):
        self.graph = {}

    def initializing_graph(self, dependencies):
        for x in dependencies:
            parent, child = x[1], x[0]
            self.graph[parent], self.graph[child] = [], []
    
    def building_graph(self, dependencies):
        for dependency in dependencies:
            parent, child = dependency[1], dependency[0]
            self.graph[parent].append(child)

def find_order(n, prereqs):
    dgraph = graph()
    dgraph.initializing_graph(prereqs)
    dgraph.building_graph(prereqs)
    indegrees = {}
    for node in dgraph.graph:
        if node not in indegrees:
            indegrees[node] = 0
        for child in dgraph.graph[node]:
            if node in dgraph.graph[child]:
                return []
            if child not in indegrees:
                indegrees[child] = 1
            else:
                indegrees[child] += 1
    sources = []
    for node in indegrees:
        if indegrees[node] == 0:
            sources.append(node)
            indegrees[node] = -1
    result = []
    while len(sources) > 0:
        node = sources.pop()
        result.append(node)
        for child in dgraph.graph[node]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                sources.append(child)
                indegrees[child] = -1
    app_num = len(result)
    while len(result) < n:
        result.append(app_num)
        app_num += 1
    return result

n = 4
prereqs = [[1,0],[2,0],[3,1],[3,2]]
print(find_order(n, prereqs))