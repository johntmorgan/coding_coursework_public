#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:13:44 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

# O(n) time
# O(n) space

def populate_next_pointers(node):
    queue, next_queue = [], []
    queue.append(node)
    while queue != []:
        while queue != []:
            node = queue.pop(0)
            if queue != []:
                node.next = queue[0]
            else:
                node.next = None
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue, next_queue = next_queue, queue
    return None

# O(n) time
# O(1) space

def connect_next_level(head):
    curr = head
    next_head = None
    prev = None

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
        curr = curr.next
    if prev:
        prev.next = None
    return next_head

def populate_next_pointers(node):
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
populate_next_pointers(bst.root)
print(get_next_node(bst.root, 50).data)