#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:04:42 2023

@author: johnmorgan
"""

# Template for binary tree node

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.diameter = 0

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0