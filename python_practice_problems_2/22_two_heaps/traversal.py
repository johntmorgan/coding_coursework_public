#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:51:47 2023

@author: johnmorgan
"""

# Template for array traversal
class traversal:
    def __init__(self):
        self.array = []
        
    def forward_traversal(self):
        for element in self.array:
            print(element)
        
    def backward_traversal(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])