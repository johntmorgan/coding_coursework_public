#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:52:35 2023

@author: johnmorgan
"""

from binary_tree import *
from binary_tree_node import *

# O(n) time, O(h) space

class MaxTreePathSum:
    def __init__(self):
        self.max_sum = float('-inf')

    def recurse_mps(self, node):
        if node is None:
            return 0
        else:
            max_left = self.recurse_mps(node.left)
            max_right = self.recurse_mps(node.right)
            left_subtree = max(0, max_left)
            right_subtree = max(0, max_right)
            compare_sum = node.data + left_subtree + right_subtree
            if compare_sum > self.max_sum:
                self.max_sum = compare_sum
            if not node.data:
                return max(left_subtree, right_subtree)
            else:
                return node.data + max(left_subtree, right_subtree)
        
    def max_path_sum(self, root):
        self.recurse_mps(root)
        return self.max_sum
    
nums = [-8,2,17,1,4,19,5]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
print(bst.root.right.data)
mtps = MaxTreePathSum()
print(mtps.max_path_sum(bst.root))

nums = [7, 3, 4, -1, -3]
bst = BinaryTree()
for num in nums:
    bst.insert(num)
mtps = MaxTreePathSum()
print(mtps.max_path_sum(bst.root))