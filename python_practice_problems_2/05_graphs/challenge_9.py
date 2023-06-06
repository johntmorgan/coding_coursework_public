#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:17:45 2023

@author: johnmorgan
"""

from Graph import Graph
from Queue import MyQueue
from Stack import MyStack

# O(E) - worst case, all edges must be traversed in one linked list to delete value

def remove_edge(graph, source, dest):
    if len(graph.array) == 0:
        return graph
    if source >= len(graph.array) or source < 0:
        return graph
    if dest >= len(graph.array) or dest < 0:
        return graph
    graph.array[source].delete(dest)
    return graph
    

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(4, 0)

graph.print_graph()
remove_edge(graph, 2, 3)
graph.print_graph()