#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:09:34 2023

@author: johnmorgan
"""

from Graph import Graph

# Inefficient, bfs from every vertex

def is_strongly_connected(graph):
    for vertex in range(graph.V):
        visited = [False] * graph.V
        to_visit = [vertex]
        while to_visit:
            visiting = to_visit.pop(0)
            visited[visiting] = True
            node = graph.graph[visiting]
            while node:
                if not visited[node.vertex]:
                    to_visit += [node.vertex]
                node = node.next
        for visit_status in visited:
            if visit_status == False:
                return False
    return True

# Course solution
# Ask if can reach every point from vertex 0
# Then transpose graph and ask same question
# Quick review this approach!

# def is_strongly_connected(graph):
#     """
#     Finds if the graph is strongly connected or not
#     :param graph: The graph
#     :return: returns True if the graph is strongly connected, otherwise False
#     """

#     result = dfs(graph, 0)
#     if graph.V != len(result):
#         return False
#     graph2 = transpose(graph)
#     result = dfs(graph2, 0)
#     if graph2.V != len(result):
#         return False

#     return True


g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,0)
g.add_edge(4,2)
print(is_strongly_connected(g))

g2 = Graph(5)
g2.add_edge(0,1)
g2.add_edge(1,2)
g2.add_edge(2,4)
g2.add_edge(3,0)
g2.add_edge(4,2)
print(is_strongly_connected(g2))