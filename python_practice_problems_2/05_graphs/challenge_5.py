#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:06:10 2023

@author: johnmorgan
"""

from Graph import Graph
from Stack import MyStack

# O(V + E)

def num_edges(graph):
    visited = []
    edges = 0
    for vertex in range(graph.vertices):
        curr_node = graph.array[vertex].get_head()
        while curr_node != None:
            edges += 1
            curr_node = curr_node.next_element
    return edges // 2

# Still O(V + E), more compact code though

def num_edges(g):
    return sum([g.array[i].length() for i in range(g.vertices)]) // 2

graph = Graph(9)
graph.add_edge(0, 2)
graph.add_edge(0, 5)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(5, 3)
graph.add_edge(5, 6)
graph.add_edge(3, 6)
graph.add_edge(6, 7)
graph.add_edge(6, 8)
graph.add_edge(6, 4)
graph.add_edge(7, 8)

print(num_edges(graph))