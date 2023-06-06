#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 18:23:32 2023

@author: johnmorgan
"""

from binary_tree_node import *
from binary_tree import *

def recurse_bt(node):
    if node is None:
        return
    else:
        recurse_bt(node.left)
        recurse_bt(node.right)
        node.left, node.right = node.right, node.left

def mirror_binary_tree(root):
    if root is not None:
        recurse_bt(root)
    return root


bt = BinaryTree()
nums = [100,50,200,25,75,125,350]
for num in nums:
    bt.insert(num)
mirror_binary_tree(bt.root)