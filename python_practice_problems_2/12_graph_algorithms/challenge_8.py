#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:29:44 2023

@author: johnmorgan
"""

from Graph3 import Graph

def remove_edge(graph, source, destination):
    """
    A function to remove an edge
    :param graph: A graph
    :param source: Source Vertex
    :param destination: Destination Vertex
    """
    deleted = False
    prior = None
    node = graph.graph[source]
    while node and not deleted:
        if node.vertex == destination:
            if prior == None:
                graph.graph[source] = node.next
            else:
                prior.next = node.next
            deleted = True
        prior = node
        node = node.next
    return bfs(graph, 0)
    

def bfs(graph, source):
    visited = [False] * graph.V
    to_visit = [source]
    result = ""
    while to_visit:
        visiting = to_visit.pop(0)
        visited[visiting] = True
        result += str(visiting)
        node = graph.graph[visiting]
        while node:
            if not visited[node.vertex]:
                to_visit += [node.vertex]
            node = node.next
    return result

g8 = Graph(5)
g8.add_edge(0,1)
g8.add_edge(0,2)
g8.add_edge(1,3)
g8.add_edge(2,4)
g8.print_graph()
print(remove_edge(g8, 0, 2))
