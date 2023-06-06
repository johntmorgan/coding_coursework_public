#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 18:12:48 2023

@author: johnmorgan
"""

from binary_tree import *

def dfs_rob(node, can_rob):
    if not node:
        return 0
    else:
        if can_rob:
            return max(node.data + dfs_rob(node.left, False) + dfs_rob(node.right, False),
                       dfs_rob(node.left, True) + dfs_rob(node.right, True))
        else:
            return dfs_rob(node.left, True) + dfs_rob(node.right, True)

def rob(root):
    can_rob = True
    max_loot = dfs_rob(root, can_rob)
    return max_loot

vals = [9,7,11,1,8,10,12]
bst = BinaryTree()
for val in vals:
    bst.insert(val)
print(rob(bst.root))