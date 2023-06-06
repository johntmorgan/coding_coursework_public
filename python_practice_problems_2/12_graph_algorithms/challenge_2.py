#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:35:57 2023

@author: johnmorgan
"""

from Graph import Graph

def dfs(graph, source):
    to_visit = [source]
    visited = [False] * graph.V
    result = ""
    while to_visit:
        visiting = to_visit.pop()
        visited[visiting] = True
        result += str(visiting)
        node = graph.graph[visiting]
        while node:
            if not visited[node.vertex]:
                to_visit.append(node.vertex)
            node = node.next
    return result
    


g = Graph(5)
g.add_edge(0,2)
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,3)
print(dfs(g, 0))