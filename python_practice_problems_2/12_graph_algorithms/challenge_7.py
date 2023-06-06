#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:09:44 2023

@author: johnmorgan
"""

from Graph2 import Graph
from copy import copy

# Helper Function of DFS. Might be useful
def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a list
    """

    graph = g
    # Create a stack for DFS
    stack = []
    # Result list
    result = []
    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next
    return result

def connected_components(graph):
    visited = [False] * graph.V
    components = []
    while False in visited:
        source = None
        curr_index = 0
        while not source and curr_index < graph.V:
            if visited[curr_index] == False:
                source = curr_index
            curr_index += 1
        component = dfs(graph, source, visited)
        component.sort()
        for index in range(len(component)):
            component[index] = int(component[index])
        components += [component]
    return components

g = Graph(7)
g.add_edge(0,1)
g.add_edge(0,3)
g.add_edge(1,0)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,1)
g.add_edge(3,2)
g.add_edge(3,0)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(6,5)
print(connected_components(g))