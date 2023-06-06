#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:50:49 2023

@author: johnmorgan
"""

# Review, easy but pattern may be tricky to derive

from binary_tree import *
from binary_tree_node import *

def flatten_tree(root):
    node = root
    while node:
        if node.left:
            target = node.right
            search = node.left
            while search.right:
                search = search.right
            search.right = target
            node.right = node.left
            node.left = None
        else:
            node = node.right
    return root


bt = BinaryTree()
nums = [3,2,17,1,4,19,5]
for num in nums:
    bt.insert(num)
node = flatten_tree(bt.root)
while node:
    print(node.data)
    node = node.right