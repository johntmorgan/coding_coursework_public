#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:03:01 2022

@author: johnmorgan
"""

def breadth_first_search(Adj, s):
    parent = [None for v in Adj]
    parent[s] = s
    level = [[s]]
    print(level[-1])
    # While prior level contains vertices
    while 0 < len(level[-1]):
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] is None:
                    parent[v] = u
                    level[-1].append(v)
    print(level)
    return parent

def unweighted_shortest_path(Adj, s, t):
    parent = breadth_first_search(Adj, s)
    if parent[t] is None:
        return None
    i = t
    path = [t]
    while i != s:
        i = parent[i]
        path.append(i)
    return path[::-1] # reverses path - could also call path.reverse()

A2 = [[1, 4, 3], [0], [3], [0, 2], [0]]
# Returns parent of each node in shortest path, preserving O(v) space
print(breadth_first_search(A2, 1))
print(unweighted_shortest_path(A2, 0, 2))