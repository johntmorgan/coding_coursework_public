#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:42:47 2023

@author: johnmorgan
"""

from Graph3 import Graph

def detect_cycle(graph):
    """
    A function to remove an edge
    :param graph: A graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    visited = [False] * graph.V
    to_visit = [0]
    while to_visit:
        visiting = to_visit.pop(0)
        visited[visiting] = True
        node = graph.graph[visiting]
        while node:
            if not visited[node.vertex]:
                to_visit += [node.vertex]
            else:
                return True
            node = node.next
    return False


g = Graph(3)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,0)
print(detect_cycle(g))

g2 = Graph(3)
g2.add_edge(0,1)
g2.add_edge(1,2)
print(detect_cycle(g2))