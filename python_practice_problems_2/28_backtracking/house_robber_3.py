#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:37:15 2023

@author: johnmorgan
"""

from binary_tree import *
from collections import deque

# Review, couldn't get this pattern
# O(n) time complexity
# O(h) space complexity

def rob(root):
   return max(depthfs(root))
   
def depthfs(root):
    if root == None:
        return [0, 0]   
    left_children = depthfs(root.left)
    right_children = depthfs(root.right)
    not_node = max(left_children) + max(right_children)
    node = root.data + left_children[1] + right_children[1]
    return [node, not_node]

vals = [9,7,11,1,8,10,12]
bst = BinaryTree()
for val in vals:
    bst.insert(val)
print(rob(bst.root))
