#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:54:51 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *
from collections import defaultdict, deque

def vertical_order(root):
    queue, next_queue = [[root, 0]], []
    columns = defaultdict(list)
    min_col, max_col = float('inf'), float('-inf')
    while queue:
        curr = queue.pop(0)
        if curr and curr[0]:
            columns[curr[1]] += [curr[0].data]
            next_queue.append([curr[0].left, curr[1] - 1])
            next_queue.append([curr[0].right, curr[1] + 1])
            if curr[1] - 1 < min_col:
                min_col = curr[1] - 1
            if curr[1] + 1 > max_col:
                max_col = curr[1] + 1
        if not queue:
            queue, next_queue = next_queue, queue
    result = []
    for col in range(min_col, max_col + 1):
        if columns[col]:
            result.append(columns[col])
    return result
    


bt = BinaryTree()
nums = [100,50,200,25,75,300,10,350,15]
for num in nums:
    bt.insert(num)
print(vertical_order(bt.root))