#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:22:50 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

# O(n)
# O(h) space, because size of call stack
# O(logn) space if balanced, up to O(n) if degenerate

def ser_recurse(node, result):
    result.append(node.data)
    if node.left:
        ser_recurse(node.left, result)
    if node.right:
        ser_recurse(node.right, result)

def serialize(root):
    result = []
    ser_recurse(root, result)
    return result

# Function to deserialize integer list into a binary tree.

def deserialize(stream):
    bst = BinaryTree()
    for node_data in stream:
        new_node = BinaryTreeNode(node_data)
        if not bst.root:
            bst.root = new_node
        else:
            parent = None
            temp_pointer = bst.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= temp_pointer.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node
    return bst.root
   


nums = [100,50,200,25,75,350]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
slist = serialize(bst.root)
print(slist)
broot = deserialize(slist)
print(broot.data)