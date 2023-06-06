#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:36:08 2023

@author: johnmorgan
"""

from Node1 import Node
from BST1 import BinarySearchTree
from BSTDisplay import *

# Iterative JM
# O(n), must visit all nodes

def findHeight(root):
    if root is None:
        return -1
    visiting = [[root, 0]]
    curr_node = visiting[0]
    while len(visiting) > 0:
        if curr_node[0].leftChild is not None:
            visiting += [[curr_node[0].leftChild, curr_node[1] + 1]]
        if curr_node[0].rightChild is not None:
            visiting += [[curr_node[0].rightChild, curr_node[1] + 1]]
        curr_node = visiting[0]
        visiting = visiting[1:]
    return curr_node[1]

# Recursive
# O(n), must visit all nodes

def findHeight(root):
    if root is None:
        return -1
    else:
        max_sub_tree_height = max(
            findHeight(root.leftChild),
            findHeight(root.rightChild))
        return 1 + max_sub_tree_height

BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(2)
BST.insert(5)
BST.insert(8)
BST.insert(12)
BST.insert(10)
BST.insert(14)
# display(BST.root)
print(findHeight(BST.root))

