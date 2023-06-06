#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:15:33 2023

@author: johnmorgan
"""

from Node1 import Node
from BST1 import BinarySearchTree
from BSTDisplay import *

# JM iterative solution
# O(log(n)) time complexity

def findAncestors(root, k):
    if root is None or (root.leftChild == None and root.rightChild == None):
        return []
    curr_node = root
    visited = []
    ancestors = []
    while curr_node.val != k:
        ancestors += [curr_node.val]
        if curr_node.val > k and curr_node.leftChild is not None:
            curr_node = curr_node.leftChild
        elif curr_node.val < k and curr_node.rightChild is not None:
            curr_node = curr_node.rightChild
        else:
            return "Value is not in tree!"
    ancestors.reverse() # can also return ancestors[::-1]
    return ancestors

# Recursive solution
# O(n) time, iterates over all tree nodes

# def findAncestors(root, k):
#     result = []
#     recfindAncestors(root, k, result)  # recursively find ancestors
#     return str(result)  # return a string of ancestors


# def recfindAncestors(root, k, result):
#     if root is None:  # check if root exists
#         return False
#     elif root.val is k:  # check if val is k
#         return True
#     recur_left = recfindAncestors(root.leftChild, k, result)
#     recur_right = recfindAncestors(root.rightChild, k, result)
#     if recur_left or recur_right:
#         # if recursive find in either left or right sub tree
#         # append root value and return true
#         result.append(root.val)
#         return True
#     return False  # return false if all failed


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
print(findAncestors(BST.root, 10))