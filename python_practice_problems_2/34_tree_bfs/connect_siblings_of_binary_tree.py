#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:49:57 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

def connect_next_level(head):
    curr = head
    next_head = None
    prev = None
    last = None

    while curr:
        if curr.left and curr.right:
            if not next_head:
                next_head = curr.left
            curr.left.next = curr.right
            if prev:
                prev.next = curr.left
            prev = curr.right
        elif curr.left:
            if not next_head:
                next_head = curr.left
            if prev:
                prev.next = curr.left
            prev = curr.left
        elif curr.right:
            if not next_head:
                next_head = curr.right
            if prev:
                prev.next = curr.right
            prev = curr.right
        if not curr.next:
            last = curr
        curr = curr.next
    if prev:
        prev.next = None
    if last:
        last.next = next_head
    return next_head

def populate_next_node_pointers(node):
    if node:
        node.next = None
        while True:
            node = connect_next_level(node)
            if not node:
                break

# Do not modify the code below
# Function to find the given node and return its next node
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
    
nums = [100,50,200,25,75,300,10,350,15]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
populate_next_node_pointers(bst.root)
print(get_next_node(bst.root, 50).data)
print(get_next_node(bst.root, 200).data)