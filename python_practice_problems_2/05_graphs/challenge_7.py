#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:29:44 2023

@author: johnmorgan
"""

from Graph import Graph
from Stack import MyStack

# O(V + E)

def check_cycle(g, curr_val, visited, parent):
    visited += [curr_val]
    curr_node = g.array[curr_val].get_head()
    while curr_node is not None:
        if curr_node.data not in visited:
            if check_cycle(g, curr_node.data, visited, curr_val):
                return True
        elif curr_node.data in visited and curr_node.data is not parent:
            return True
        curr_node = curr_node.next_element
    return False

def is_tree(g):
    visited = []
    source = 0
    if check_cycle(g, source, visited, -1):
        return False
    return len(visited) == g.vertices

tree = Graph(5)
tree.add_edge(0, 1)
tree.add_edge(0, 2)
tree.add_edge(0, 3)
tree.add_edge(3, 4)
tree.add_edge(1, 0)
tree.add_edge(2, 0)
tree.add_edge(3, 0)
tree.add_edge(4, 3)

print(is_tree(tree))

tree = Graph(6)
tree.add_edge(0, 1)
tree.add_edge(0, 2)
tree.add_edge(0, 3)
tree.add_edge(1, 0)
tree.add_edge(2, 0)
tree.add_edge(3, 0)
tree.add_edge(3, 4)
tree.add_edge(4, 3)
tree.add_edge(4, 5)
tree.add_edge(5, 4)

print(is_tree(tree))

cyclic = Graph(4)
cyclic.add_edge(0, 1)
cyclic.add_edge(0, 3)
cyclic.add_edge(3, 2)
cyclic.add_edge(2, 0)
cyclic.add_edge(1, 0)
cyclic.add_edge(3, 0)
cyclic.add_edge(2, 3)
cyclic.add_edge(0, 2)

print(is_tree(cyclic))

discon = Graph(5)
discon.add_edge(0, 2)
discon.add_edge(0, 3)
discon.add_edge(3, 4)
discon.add_edge(2, 0)
discon.add_edge(3, 0)
discon.add_edge(4, 3)

print(is_tree(discon))