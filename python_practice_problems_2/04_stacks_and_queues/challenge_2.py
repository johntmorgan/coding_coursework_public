#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:00:41 2023

@author: johnmorgan
"""

# All operations O(1) time

class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.stack_list = [None for _ in range(size)]
        self.stack_list_size = size
        self.stack2_index = 0
        
    # Insert Value in First Stack
    def push1(self, value):
        for idx in range(0, self.stack2_index):
            self.stack_list[idx + 1] = self.stack_list[idx]
        self.stack2_index += 1
        self.stack_list[0] = value

    # Insert Value in Second Stack
    def push2(self, value):
        for idx in range(self.stack2_index, self.stack_list_size - 1):
            self.stack_list[idx + 1] = self.stack_list[idx]
        self.stack_list[self.stack2_index] = value

    # Return and remove top Value from First Stack
    def pop1(self):
        value = self.stack_list[0]
        for idx in range(1, self.stack_list_size - 1):
            self.stack_list[idx - 1] = self.stack_list[idx]
        self.stack_list[self.stack_list_size - 1] = None
        self.stack2_index -= 1
        return value

    # Return and remove top Value from Second Stack
    def pop2(self):
        value = self.stack_list[self.stack2_index]
        for idx in range(self.stack2_index, self.stack_list_size - 1):
            if idx > 0:
                self.stack_list[idx - 1] = self.stack_list[idx]
                self.stack_list[self.stack_list_size - 1] = None
        return value

two = TwoStacks(10)

two.push1(1)
two.push2(2)
print(two.pop1())
print(two.pop2())