#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:53:33 2023

@author: johnmorgan
"""

# O(n) - each node visited 2 times at most


from binary_tree import *
from binary_tree_node import *

class MaxTreePathSum:
    def __init__(self):
        self.max_sum = float('-inf')

    def recurse_mps(self, node):
        if node is None:
            return 0
        else:
            left_sum = self.recurse_mps(node.left)
            right_sum = self.recurse_mps(node.right)
            if node.data + left_sum + right_sum > self.max_sum:
                self.max_sum = node.data + left_sum + right_sum
            return node.data + max(left_sum, right_sum)

    def max_path_sum(self, root):
        self.recurse_mps(root)
        return self.max_sum
    
    
bt = BinaryTree()
nums = [-8,2,17,1,4,19,5]
for num in nums:
    bt.insert(num)
mtps = MaxTreePathSum()
print(mtps.max_path_sum(bt.root))
        
        