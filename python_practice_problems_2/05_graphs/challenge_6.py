#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:20:03 2023

@author: johnmorgan
"""

from Graph import Graph
from Stack import MyStack

def check_path(graph, source, destination):
    v_stack = MyStack()
    v_stack.push(source)
    visited = []
    while not v_stack.is_empty():
        curr_val = v_stack.pop()
        if curr_val not in visited:
            visited.append(curr_val)
            curr_node = graph.array[curr_val].get_head()
            while curr_node is not None:
                if curr_node.data == destination:
                    return True
                v_stack.push(curr_node.data)
                curr_node = curr_node.next_element
    return False
        
            
    

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

print(check_path(graph, 0, 7))
print(check_path(graph, 0, 8))
print(check_path(graph, 0, 5))
print(check_path(graph, 0, 1))
print(check_path(graph, 1, 2))