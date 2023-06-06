#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:39:01 2023

@author: johnmorgan
"""

from Node1 import Node
from BST1 import BinarySearchTree
from BSTDisplay import *

# Iterative solution
# Time complexity is O(h)
# Worst case, skewed tree, O(n)
# If balanced, O(log(n))

# def findMin(root):
#     if root is None:
#         return None
#     curr_node = root
#     while curr_node.leftChild != None:
#         curr_node = curr_node.leftChild
#     return curr_node.val

# Recursive solution - also coded this - JM
# Same time complexity as iterative

def findMin(root):
    if root is None:
        return None
    if root.leftChild == None:
        return root.val
    else:
        return findMin(root.leftChild)
        

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
print(findMin(BST.root))