#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:07:53 2023

@author: johnmorgan
"""

from Graph import Graph
from Queue import MyQueue

# O(V + E)

def find_min(g, source, destination):
    result = []
    v_queue = MyQueue()
    v_queue.enqueue([source, 0])
    while not v_queue.is_empty():
        vertex = v_queue.dequeue()
        curr_node = g.array[vertex[0]].get_head()
        while curr_node != None:
            if curr_node.data == destination:
                return vertex[1] + 1
            if curr_node.data not in result:
                v_queue.enqueue([curr_node.data, vertex[1] + 1])
            curr_node = curr_node.next_element
    return -1


graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(3, 5)
graph.add_edge(5, 4)
graph.add_edge(2, 4)

print(find_min(graph, 0, 4))
    