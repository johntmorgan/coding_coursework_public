#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:53:09 2023

@author: johnmorgan
"""

from Node1 import Node
from BST1 import BinarySearchTree
from BSTDisplay import *

# JM iterative
# O(n)

def findKNodes(root, k):
    if root is None:
        return 
    curr_node = root
    curr_index = 0
    visited = [[curr_node, 0]]
    target_nodes = []
    while visited[-1][1] <= k:
        if curr_node.leftChild is not None:
            visited += [[curr_node.leftChild, visited[curr_index][1] + 1]]
        if curr_node.rightChild is not None:
            visited += [[curr_node.rightChild, visited[curr_index][1] + 1]]
        if visited[curr_index][1] == k:
            target_nodes += [curr_node.val]
        curr_index += 1
        curr_node = visited[curr_index][0]
    return target_nodes

# Recursive O(n)

def findKNodes(root, k):
    res = []
    findK(root, k , res)
    return str(res)

def findK(root, k, res):
    if root is None:
        return
    if k == 0:
        res.append(root.val)
    else:
        findK(root.leftChild, k - 1, res)
        findK(root.rightChild, k - 1, res)

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
print(findKNodes(BST.root, 2))
