#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:39:22 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

# Function to populate same level pointers
def populate_next_pointers(root):
    queue, next_queue = [root], []
    prior = None
    while queue:
        curr = queue.pop(0)
        if curr:
            next_queue.append(curr.left)
            next_queue.append(curr.right)
            if prior:
                prior.next = curr
        if not queue:
            queue, next_queue = next_queue, queue
            prior = None
        elif curr:
            prior = curr
    return 

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

bt = BinaryTree()
nums = [100,50,200,25,75,300,10,350,15]
for num in nums:
    bt.insert(num)
print(populate_next_pointers(bt.root))

print(get_next_node(bt.root, 75).data)
