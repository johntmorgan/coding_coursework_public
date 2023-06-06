#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:36:49 2023

@author: johnmorgan
"""

from Graph import Graph
from Stack import MyStack

# Brute force
# O(V(V + E))

def dfs_subtree_traversal(g, source):
    result = []
    v_stack = MyStack()
    v_stack.push(source)
    while not v_stack.is_empty():
        vertex = v_stack.pop()
        if str(vertex) not in result:
            result.append(str(vertex))
            curr_node = g.array[vertex].get_head()
            while curr_node != None:
                if str(curr_node.data) not in result:
                    v_stack.push(curr_node.data)
                curr_node = curr_node.next_element
    return result
    
def find_mother_vertex(g):
    for mother in range(g.vertices):
        if len(dfs_subtree_traversal(g, mother)) == g.vertices:
            return mother
    return None

# O(V + E)
# Based on Kosaraju's Strongly Connected Component Theorem

def find_mother_vertex(g):
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False]*(g.vertices)
    # To store last finished vertex (or mother vertex)
    last_v = 0
    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if not visited[i]:
            perform_DFS(g, i, visited)
            last_v = i

    # If there exist mother vertex (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.
    visited = [False]*(g.vertices)
    perform_DFS(g, last_v, visited)
    if any (not i for i in visited): # any() func iterates over a list
        return -1
    else:
        return last_v

# A recursive function to print DFS starting from v
def perform_DFS(g, node, visited):
    # Mark the current node as visited and print it
    visited[node] = True
    # Recur for all the vertices adjacent to this vertex
    temp = g.array[node].head_node
    while temp:
        if not visited[temp.data]:
            perform_DFS(g, temp.data, visited)
        temp = temp.next_element

graph = Graph(4)
graph.add_edge(3, 0)
graph.add_edge(3, 1)
graph.add_edge(0, 1)
graph.add_edge(1, 2)

print(find_mother_vertex(graph))