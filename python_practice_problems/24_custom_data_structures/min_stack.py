#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:56:44 2023

@author: johnmorgan
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) > 0 and self.min_stack[-1] > val:
            self.min_stack.append(val)
        elif len(self.min_stack) > 0:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
            
    def pop(self):
        if len(self.stack) > 0:
            self.min_stack.pop()
            return self.stack.pop()
        
    def min_number(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None