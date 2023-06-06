#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:33:20 2023

@author: johnmorgan
"""

from stack import MainStack

# O(1) all
# O(2n) space -> O(n) space

class MinStack:
    # Initialize min and main stack here
    def __init__(self):
        self.main_stack = MainStack()
        self.min_stack = MainStack()

    # Remove and returns value from the stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes values into the stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or value < self.min_stack.top():
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())

    # Returns minimum value from stack
    def min_number(self):
        if self.min_stack.is_empty():
            return None
        else:
            return self.min_stack.top()
    
    
mins = MinStack()
mins.push(9)
mins.push(3)
print(mins.pop())
mins.push(4)
print(mins.pop())
mins.push(5)
print(mins.min_number())