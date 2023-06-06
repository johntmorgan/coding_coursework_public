#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 14:52:15 2023

@author: johnmorgan
"""

def components_count_in_graph(n, edges):
    components = 0
    visited = []
    for edge in edges:
        start = edge[0]
        end = edge[1]
        if start in visited or end in visited:
            if start not in visited:
                visited.append(start)
            if end not in visited:
                visited.append(end)
        else:
            visited.append(start)
            visited.append(end)
            components += 1
    single_nodes = n - len(visited)
    components += single_nodes
    return components
    
    
    
n = 5
edges = [[0,1],[1,2],[3,4]]