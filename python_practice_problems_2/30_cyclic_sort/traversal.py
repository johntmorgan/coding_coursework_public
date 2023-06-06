#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:47:49 2023

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
        for element in reversed(self.array):
            print(element)