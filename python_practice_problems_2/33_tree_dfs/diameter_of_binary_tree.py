#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:47:10 2023

@author: johnmorgan
"""

from binary_tree_node import *
from binary_tree import *

# Solution code

# O(n) time
# O(n) space - recursive stack can grow up to n

def diameter_helper(node, diameter):
    if node is None:
        return 0, diameter
    else:
        lh, diameter = diameter_helper(node.left, diameter)
        rh, diameter = diameter_helper(node.right, diameter)
        diameter = max(diameter, lh + rh)
        return max(lh, rh) + 1, diameter

def diameter_of_binaryTree(root):
    diameter = 0
    if not root:
        return 0
    _, diameter = diameter_helper(root, diameter)
    return diameter


# My kludgy solution

def recurse_tree(node, stack, max_diam):
    curr = stack.pop()
    if node.left:
        stack.append(node)
        stack.append(node.left)
        recurse_tree(node.left, stack, max_diam)
        node.left_height = 1 + max(node.left.left_height, node.left.right_height)
    else:
        node.left_height = 0
    if node.right:
        stack.append(node.right)
        recurse_tree(node.right, stack, max_diam)
        node.right_height = 1 + max(node.right.left_height, node.right.right_height)
    else:
        node.right_height = 0
    if node.left:
        left_diameter = node.left.diameter
    else:
        left_diameter = 0
    if node.right:
        right_diameter = node.right.diameter
    else:
        right_diameter = 0
    node.diameter = max(left_diameter, right_diameter, node.left_height + node.right_height)
    if node.diameter > max_diam:
        max_diam = node.diameter
    return max_diam
        
def diameter_of_binaryTree(root):
    stack, max_diam = [root], 0
    max_diam = recurse_tree(root, stack, max_diam)
    return max_diam


nums = [1,2,3,4,5,6]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
print(diameter_of_binaryTree(bst.root))

