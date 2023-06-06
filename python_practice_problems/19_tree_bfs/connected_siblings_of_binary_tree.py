#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 18:13:42 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

def populate_next_node_pointers(root):
    queue, next_queue = [root], []
    prior = None
    while queue:
        curr = queue.pop(0)
        if curr:
            next_queue.append(curr.left)
            next_queue.append(curr.right)
            if prior:
                prior.next = curr
            prior = curr
        if not queue:
            queue, next_queue = next_queue, queue
    

bt = BinaryTree()
nums = [100,50,200,25,75,300,10,350,15]
for num in nums:
    bt.insert(num)
populate_next_node_pointers(bt.root)
    
def get_next_node(node, node_data):
    # Performing Binary Search
    while node and node_data != node.data:
        if node_data < node.data:
            node = node.left
        else:
            node = node.right

    # If node is not found return -1 else return its next node
    if not node:
        non_existing_node = BinaryTreeNode(-1)
        return non_existing_node
    else:
        return node.next
    
node_data = 200
print(get_next_node(bt.root, node_data).data)