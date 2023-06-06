#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 18:25:14 2023

@author: johnmorgan
"""

from collections import deque
from binary_tree import *

# O(n) space and time - queue may hold up to ceil(n/2) nodes -> O(n)

def level_order_traversal(root):
    result = ""
    curr, nxt = [], []
    if root is None:
        return None
    curr.append(root)
    while curr != []:
        while curr != []:
            print(curr)
            node = curr.pop(0)
            if len(curr) > 0:
                result += str(node.data)
                result += ", "
            else:
                result += str(node.data)
            if node.left:
                nxt.append(node.left)
            if node.right:
                nxt.append(node.right)
        if len(nxt) > 0:
            result += " : "
        curr, nxt = nxt, curr
    return result

nums = [100,50,200,25,75,300,10,350,15]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
print(level_order_traversal(bst.root))