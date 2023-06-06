#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:30:04 2023

@author: johnmorgan
"""

from binary_tree_node import *
from binary_tree import *

def traverse_tree(root, sort_list):
    if root == None:
        return
    else:
        traverse_tree(root.left, sort_list)
        sort_list.append(root.data)
        traverse_tree(root.right, sort_list)

def kth_smallest_element(root, k):
    sort_list = []
    traverse_tree(root, sort_list)
    return sort_list[k - 1]
    
    

bst = BinaryTree()
nums = [2, 1, 3]
k = 2
for elem in nums:
    bst.insert(elem)
print(kth_smallest_element(bst.root, k))


