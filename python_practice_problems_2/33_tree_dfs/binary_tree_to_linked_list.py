#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:11:37 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *
        
# O(n)
# O(1) space
# Review

def flatten_tree(root):
    if not root:
        return
    curr = root
    while curr:
        if curr.left:
            last = curr.left
            while last.right:
                last = last.right
            last.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right
    return root


nums = [3,2,17,1,4,19,5]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
# print(flatten_tree(bst.root))
# print(bst.root.data)
# print(bst.root.right.data)
# print(bst.root.right.right.data)
# print(bst.root.right.right.right.data)
# print(bst.root.right.right.right.right.data)
# print(bst.root.right.right.right.right.right.data)