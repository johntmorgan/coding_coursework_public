#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 18:06:08 2023

@author: johnmorgan
"""

from binary_tree_node import *
from binary_tree import *

def ser_recurse(node, result):
    if node is None:
        return
    else:
        result.append(node.data)
        ser_recurse(node.left, result)
        ser_recurse(node.right, result)

def serialize(root):
    result = []
    ser_recurse(root, result)
    return result
    
    
def deserialize(stream):
    bt = BinaryTree()
    for node_data in stream:
        new_node = BinaryTreeNode(node_data)
        if not bt.root:
            bt.root = new_node
        else:
            parent = bt.root
            temp_pointer = bt.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= parent.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node
    return bt.root


bt = BinaryTree()
nums = [100,50,200,25,75,350]
for num in nums:
    bt.insert(num)
result = serialize(bt.root)
print(result)
deserialize(result)


