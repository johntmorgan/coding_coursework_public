#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:13:38 2023

@author: johnmorgan
"""

# Review non-modifying solution

from binary_tree_node import *
from binary_tree import *

# Without modifying node

def diameter_helper(node, diameter_res):
    if node is None:
        return 0, diameter_res
    else:
        # JM: isn't there an issue where l and r diameter res could differ?
        lh, diameter_res = diameter_helper(node.left, diameter_res)
        rh, diameter_res = diameter_helper(node.right, diameter_res)
        diameter_res = max(diameter_res, lh + rh)
        return max(lh, rh) + 1, diameter_res

def diameter_of_binaryTree(root):
    diameter_res = 0
    if not root:
        return 0
    _, diameter_res = diameter_helper(root, diameter_res)
    return diameter_res

# My easy to read sol'n, modify to store height, diameter on each node

# def recurse(node):
#     if node.left and node.right:
#         recurse(node.left)
#         recurse(node.right)
#         node.height = 1 + max(node.left.height, node.right.height)
#         node.diameter = max(node.left.diameter, node.right.diameter, 
#                             2 + node.left.height + node.right.height)
#     elif node.left:
#         recurse(node.left)
#         node.height = 1 + node.left.height
#         node.diameter = max(node.left.diameter, 1 + node.left.height)
#     elif node.right:
#         recurse(node.right)
#         node.height = 1 + node.right.height
#         node.diameter = max(node.right.diameter, 1 + node.right.height)
#     return node.diameter

# def diameter_of_binaryTree(root):
#     return recurse(root)

bt = BinaryTree()
nums = [3,2,17,1,4,19,5]
for num in nums:
    bt.insert(num)
print(diameter_of_binaryTree(bt.root))