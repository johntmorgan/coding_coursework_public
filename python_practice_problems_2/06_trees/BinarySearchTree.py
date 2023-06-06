#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:20:37 2023

@author: johnmorgan
"""

from Node import Node

class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)
        
    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True
        
    def delete(self, val):
        if self.root is not None:
            self.root == self.root.delete(val)
            