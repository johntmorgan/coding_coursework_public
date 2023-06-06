#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:52:16 2023

@author: johnmorgan
"""

from collections import deque
from binary_tree import *

def zigzag_level_order(root):
    result = []
    curr, nxt = [], []
    if root is None:
        return None
    curr.append(root)
    while curr != []:
        level = []
        while curr != []:
            node = curr.pop(0)
            level.append(node.data)
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        result.append(level)
        curr, nxt = nxt, curr
        curr.reverse()
    return result

nums = [100,50,200,25,75,300,10,350,15]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
print(zigzag_level_order(bst.root))
