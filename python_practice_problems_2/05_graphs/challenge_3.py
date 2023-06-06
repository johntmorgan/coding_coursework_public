#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:04:09 2023

@author: johnmorgan
"""

from Graph import Graph
from Stack import MyStack

def detect_cycle(g):
    if g.vertices == 0:
        return False
    source = None
    array_start = 0
    while source == None:
        source_node = g.array[array_start].get_head()
        if source_node is not None:
            source = source_node.data
        array_start += 1
    v_stack = MyStack()
    v_stack.push(source)
    visited = []
    while not v_stack.is_empty():
        vertex = v_stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            curr_node = g.array[vertex].get_head()
            while curr_node != None:
                if curr_node.data in visited:
                    return True
                v_stack.push(curr_node.data)
                curr_node = curr_node.next_element
    return False

    
    


cyclic_graph = Graph(3)
cyclic_graph.add_edge(0, 1)
cyclic_graph.add_edge(1, 2)
cyclic_graph.add_edge(2, 0)
print(detect_cycle(cyclic_graph))

acyclic_graph = Graph(5)
acyclic_graph.add_edge(0, 1)
acyclic_graph.add_edge(0, 2)
acyclic_graph.add_edge(1, 3)
acyclic_graph.add_edge(1, 4)

print(detect_cycle(acyclic_graph))