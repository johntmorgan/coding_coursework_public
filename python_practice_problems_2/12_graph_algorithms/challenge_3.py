#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:42:08 2023

@author: johnmorgan
"""

from Graph import Graph

def number_of_nodes(graph, level):
    visited = [False] * graph.V
    levels = [1] * graph.V
    to_visit = [0]
    while to_visit:
        visiting = to_visit.pop(0)
        visited[visiting] = True
        node = graph.graph[visiting]
        while node:
            if not visited[node.vertex]:
                to_visit += [node.vertex]
                levels[node.vertex] = levels[visiting] + 1
            node = node.next
    num_level = 0
    for node_level in levels:
        if node_level == level:
            num_level += 1
    return num_level

# Use visiting to store

def number_of_nodes(graph, level):
    visited = [0] * graph.V
    visited[0] = 1
    to_visit = [0]
    while to_visit:
        visiting = to_visit.pop(0)
        node = graph.graph[visiting]
        while node:
            if visited[node.vertex] == 0:
                to_visit += [node.vertex]
                visited[node.vertex] = visited[visiting] + 1
            node = node.next
    result = 0
    for node_level in visited:
        if node_level == level:
            result += 1
    return result
       
g = Graph(5)
g.add_edge(0,2)
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,3)
print(number_of_nodes(g, 1))
print(number_of_nodes(g, 2))
print(number_of_nodes(g, 3))
print(number_of_nodes(g, 4))