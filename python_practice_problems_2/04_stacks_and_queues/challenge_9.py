#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:35:05 2023

@author: johnmorgan
"""

from MyStack6 import MyStack

# O(1) for min() return - just track min solution
# However, is O(n) to update when popping elements
# But does save on space complexity - only one stack!

# class MinStack:
#     def __init__(self):
#         self.stack_list = []
#         self.stack_size = 0
#         self.set_min_val()
    
#     def push(self, value):
#         self.stack_size += 1
#         self.stack_list.append(value)
#         if value < self.min_val:
#             self.min_val = value

#     def pop(self):
#         if self.is_empty():
#             self.min_val = float('inf')
#             return None
#         popped = self.stack_list.pop()
#         self.stack_size -= 1
#         if popped == self.min_val:
#             self.set_min_val()
#         return popped

#     def min(self):
#         return self.min_val
    
#     def set_min_val(self):
#         new_min = float('inf')
#         for elem in self.stack_list:
#             if elem < new_min:
#                 new_min = elem
#         self.min_val = new_min

#     def is_empty(self):
#         return self.stack_size == 0

#     def peek(self):
#         if self.is_empty():
#             return None
#         return self.stack_list[-1]

#     def size(self):
#         return self.stack_size

# O(1) for min() return - two stack solution with MinStack

class MinStack:
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > (value):
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())

    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        else:
            return None
    

min_stack = MinStack()
min_stack.push(9)
min_stack.push(3)
min_stack.push(1)
min_stack.push(4)
min_stack.push(2)
min_stack.push(5)
print(min_stack.min())
min_stack.pop()
print(min_stack.min())
min_stack.pop()
min_stack.pop()
min_stack.pop()
print(min_stack.min())

