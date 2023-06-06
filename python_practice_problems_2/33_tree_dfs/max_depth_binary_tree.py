#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:18:51 2023

@author: johnmorgan
"""

from binary_tree import *
from collections import deque

def recurse_depth(node, max_depth, curr_depth):
    if node is None:
        return 0
    else:
        curr_depth = 1 + max(recurse_depth(node.left, max_depth, curr_depth),
            recurse_depth(node.right, max_depth, curr_depth))
        if curr_depth > max_depth:
            max_depth = curr_depth
        return curr_depth
    return max_depth

def max_depth(root):
    max_depth, curr_depth = 0, 0
    max_depth = recurse_depth(root, max_depth, curr_depth)
    return max_depth

nums = [9,7,20,3,15]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
print(max_depth(bst.root))