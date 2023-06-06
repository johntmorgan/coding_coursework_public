#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:07:17 2023

@author: johnmorgan
"""

from Graph import Graph

def transpose(graph):
    transpose = Graph(5)
    visited = [False] * graph.V
    to_visit = [0]
    while to_visit:
        visiting = to_visit.pop(0)
        visited[visiting] = True
        node = graph.graph[visiting]
        while node:
            if not visited[node.vertex]:
                to_visit += [node.vertex]
                transpose.add_edge(node.vertex, visiting)
            node = node.next
    return transpose

g = Graph(5)
g.add_edge(0,2)
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,3)
g.print_graph()
transpose(g).print_graph()
