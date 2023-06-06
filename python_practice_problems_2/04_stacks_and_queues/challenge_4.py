#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:44:24 2023

@author: johnmorgan
"""

from Stack3 import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //returns boolean


# class NewQueue:
#     def __init__(self):
#         self.main_stack = MyStack()
#         self.store_stack = MyStack()

#     # O(n) complexity

#     def enqueue(self, value):
#         if not self.main_stack.is_empty():
#             self.store_stack.push(self.main_stack.pop())
#         self.main_stack.push(value)
#         if not self.store_stack.is_empty():
#             self.main_stack.push(self.store_stack.pop())

#     # O(1) complexity

#     def dequeue(self):
#         if self.main_stack.is_empty():
#             return None
#         else:
#             return self.main_stack.pop()

# Better, do work in dequeue
# Do not have to reorder stacks each time
    
class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.store_stack = MyStack()

    # O(1) complexity

    def enqueue(self, value):
        self.main_stack.push(value)
    
    # Often O(1) complexity

    def dequeue(self):
        if self.store_stack.is_empty() and self.main_stack.is_empty():
            return None
        if not self.store_stack.is_empty():
            return self.store_stack.pop()
        while not self.main_stack.is_empty():
            self.store_stack.push(self.main_stack.pop())
        return self.store_stack.pop()

queue = NewQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())