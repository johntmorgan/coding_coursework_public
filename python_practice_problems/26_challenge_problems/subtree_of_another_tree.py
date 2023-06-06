#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:14:33 2023

@author: johnmorgan
"""

from binary_tree_node import BinaryTreeNode
from binary_tree import BinaryTree

def recur_compare_trees(node, subnode):
    if not node and not subnode:
        return True
    if subnode and not node:
        return False
    if node and not subnode:
        return False
    if node.data != subnode.data:
        return False
    else:
        left = recur_compare_trees(node.left, subnode.left)
        right = recur_compare_trees(node.right, subnode.right)
    return left and right
    

def subtree(node, sub_node):
    if not node:
        return False
    if node.data == sub_node.data:
        subtree_found = recur_compare_trees(node, sub_node)
        if subtree_found:
            return True
    left_tree, right_tree = False, False
    if node.left:
        left_tree = subtree(node.left, sub_node)
    if node.right:
        right_three = subtree(node.right, sub_node)
    return left_tree or right_tree
