#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:06:20 2023

@author: johnmorgan
"""

from binary_tree import *
from collections import deque

def zigzag_level_order(root):
    queue = deque()
    next_queue = deque()
    result = []
    queue.append(root)
    level_count = 0
    level_arr = []
    while queue:
        if level_count % 2 == 0:
            node = queue.pop()
        else:
            node = queue.popleft()
        if node:
            level_arr.append(node.data)
            next_queue.append(node.left)
            next_queue.append(node.right)
        if not queue:
            queue, next_queue = next_queue, queue
            if level_arr:
                result.append(level_arr)
            level_arr = []
    return result
        
bt = BinaryTree()
nums = [9,7,20,3,15]
for num in nums:
    bt.insert(num)
print(zigzag_level_order(bt.root))