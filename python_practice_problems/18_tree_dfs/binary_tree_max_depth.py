#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:29:29 2023

@author: johnmorgan
"""

from binary_tree import *
from collections import deque

def recurse_depth(node):
    if not node:
        return 0
    else:
        left_depth = recurse_depth(node.left)
        right_depth = recurse_depth(node.right)
        return 1 + max(left_depth, right_depth)

def max_depth(root):
    return recurse_depth(root)

bt = BinaryTree()
nums = [9,7,20,3,15,4,5]
for num in nums:
    bt.insert(num)
print(max_depth(bt.root))