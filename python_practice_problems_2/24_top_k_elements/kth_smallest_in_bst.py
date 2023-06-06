#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 13:41:05 2023

@author: johnmorgan
"""

from binary_tree_node import *
from binary_tree import *

def kth_smallest_element(root, k):
    stack = []
    output = []
    visited = set()
    node = root
    stack.append(node)
    while stack != []:
        node = stack.pop()
        if node.right is not None and node.right not in visited and node.left not in visited:
            stack.append(node.right)
        if node.left is not None and node.left not in visited:
            stack.append(node)
            stack.append(node.left)
        else:
            output.append(node.data)
            visited.add(node)
    print(output)
    return(output[k - 1])

bst = BinaryTree()
input_arr = [3, 1, 4, 2]
for elem in input_arr:
    bst.insert(elem)
k = 1
print(kth_smallest_element(bst.root, k))