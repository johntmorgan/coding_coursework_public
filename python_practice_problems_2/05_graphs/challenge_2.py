#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:40:32 2023

@author: johnmorgan
"""

from Graph import Graph
from Stack import MyStack

# O(V + E) - traverse whole graph once

def dfs_subtree_traversal(g, source, result):
    new_nodes = []
    v_stack = MyStack()
    v_stack.push(source)
    while not v_stack.is_empty():
        vertex = v_stack.pop()
        if vertex not in result and vertex not in new_nodes:
            new_nodes.append(str(vertex))
            curr_node = g.array[vertex].get_head()
            while curr_node != None:
                if str(curr_node.data) not in result:
                    v_stack.push(curr_node.data)
                curr_node = curr_node.next_element
    return new_nodes
    

def dfs_traversal(g, source):
    result = []
    result += dfs_subtree_traversal(g, source, result)
    for start_val in range(g.vertices):
        if str(start_val) not in result:
            result += dfs_subtree_traversal(g, start_val, result)
    return "".join(result)

graph = Graph(7)
graph.add_edge(1, 3)
graph.add_edge(1, 2)
graph.add_edge(2, 5)
graph.add_edge(2, 4)
graph.add_edge(3, 6)

print(dfs_traversal(graph, 1))