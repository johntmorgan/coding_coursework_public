#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:39:23 2023

@author: johnmorgan
"""

from collections import deque
from binary_tree import *

def level_order_traversal(root):
    if not root:
        return None
    queue = deque()
    next_queue = deque()
    level = 0
    result = ""
    queue.append(root)
    while queue:
        curr = queue.popleft()
        if curr:
            next_queue.append(curr.left)
            next_queue.append(curr.right)
            result += str(curr.data)
            result += ", "
        if not queue:
            result = result[:-2]
            if next_queue:
                result += " : "
                queue, next_queue = next_queue, queue
    return result.strip()
        

bt = BinaryTree()
nums = [100,50,200,25,75,300,10,350,15]
for num in nums:
    bt.insert(num)
print(level_order_traversal(bt.root))