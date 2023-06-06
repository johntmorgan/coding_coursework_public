#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:37:08 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

# Time O(n)
# Space O(h) - depth of stack

def recurse_bst(node):
    node.left, node.right = node.right, node.left
    if node.left:
        recurse_bst(node.left)
    if node.right:
        recurse_bst(node.right)

def mirror_binary_tree(root):
    if root is not None:
        recurse_bst(root)
    return(root)


nums = [100,50,200,25,75,350]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
root = mirror_binary_tree(bst.root)
