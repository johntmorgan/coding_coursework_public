#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 13:17:37 2023

@author: johnmorgan
"""

from Graph import Graph
from Queue import MyQueue

# O(V + E) - traverse whole graph once

def bfs_traversal(g, source):
    result = []
    v_queue = MyQueue()
    v_queue.enqueue(source)
    while not v_queue.is_empty():
        vertex = v_queue.dequeue()
        result.append(str(vertex))
        curr_node = g.array[vertex].get_head()
        while curr_node != None:
            if str(curr_node.data) not in result:
                v_queue.enqueue(curr_node.data)
            curr_node = curr_node.next_element
    return "".join(result)

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)

print(bfs_traversal(graph, 0))