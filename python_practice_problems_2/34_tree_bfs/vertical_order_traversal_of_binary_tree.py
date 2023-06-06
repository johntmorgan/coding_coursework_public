#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:34:06 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *
from collections import defaultdict, deque

# Time complexity O(n)
# Spac complexity O(n) - hash map, queue

def vertical_order(root):
    if not root:
        return None
    curr, nxt = [[root, 0]], []
    col_dict = {}
    max_col, min_col = 0, 0
    while curr != []:
        while curr != []:
            node = curr.pop(0)
            if node[1] in col_dict.keys():
                col_dict[node[1]] = col_dict[node[1]] + [node[0].data]
            else:
                col_dict[node[1]] = [node[0].data]
            if node[0].left:
                nxt.append([node[0].left, node[1] - 1])
                if min_col > node[1] - 1:
                    min_col = node[1] - 1
            if node[0].right:
                nxt.append([node[0].right, node[1] + 1])
                if max_col < node[1] + 1:
                    max_col = node[1] + 1
        curr, nxt = nxt, curr
    result = []
    for col in range(min_col, max_col + 1):
        result.append(col_dict[col])
    return result
    

nums = [100,50,200,25,75,300,10,350,15]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
print(vertical_order(bst.root))