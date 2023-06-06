#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:28:49 2023

@author: johnmorgan
"""

from Graph import Graph

# Works on my machine but not in test suite

# def find_all_paths(graph, source, destination):
#     transpose = Graph(6)
#     visited = [False] * graph.V
#     to_visit = [source]
#     while to_visit:
#         visiting = to_visit.pop(0)
#         visited[visiting] = True
#         node = graph.graph[visiting]
#         while node:
#             if not visited[node.vertex]:
#                 to_visit += [node.vertex]
#                 transpose.add_edge(node.vertex, visiting)
#             node = node.next
#     to_visit = [destination]
#     paths = [[5]]
#     while to_visit:
#         visiting = to_visit.pop(0)
#         if visiting != source:
#             curr_path = paths.pop(0)
#         visited[visiting] = True
#         node = transpose.graph[visiting]
#         while node:
#             to_visit += [node.vertex]
#             paths += [[node.vertex] + curr_path]
#             node = node.next
#     result = []
#     for path in paths:
#         if path[0] == source:
#             result.append(path)
#     return result

def find_all_paths(graph, source, destination):
    to_visit = [source]
    paths = [[0]]
    while to_visit:
        visiting = to_visit.pop(0)
        curr_path = paths.pop(0)
        node = graph.graph[visiting]
        while node:
            if visiting != destination:
                to_visit.append(node.vertex)
                paths.append(curr_path + [node.vertex])
                node = node.next
        if curr_path[-1] == destination:
            paths.append(curr_path)
    return paths

# Course solution, review needed

import copy  # For deep copy if needed

def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    # Mark the current node as visited and store in path
    visited[source] = True
    path.append(source)

    # If current vertex is same as destination, then print
    # stores the current path in 2D list (Deep copy)
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        while graph.graph[source] is not None:
            i = graph.graph[source].vertex

            if not visited[i]:
                find_all_paths_recursive(graph, i, destination, visited, path, paths)

            graph.graph[source] = graph.graph[source].next
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[source] = False


def find_all_paths(graph, source, destination):
    visited = [False] * (graph.V)
    paths = []
    path = []
    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths

g = Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(4,5)
g.print_graph()
print(find_all_paths(g, 0, 5))
