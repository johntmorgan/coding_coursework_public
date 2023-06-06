#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:02:45 2023

@author: johnmorgan
"""

from Stack3 import MyStack

# O(n^2) time complexity

# def sort_stack(stack):
#     temp_stack = MyStack()
#     while not stack.is_empty():
#         value = stack.pop()
#         if temp_stack.peek() is not None and temp_stack.peek() <= value:
#             temp_stack.push(value)
#         else:
#             while not temp_stack.is_empty() and temp_stack.peek() > value:
#                 stack.push(temp_stack.pop())
#             temp_stack.push(value)
#     while not temp_stack.is_empty():
#         stack.push(temp_stack.pop())
#     return stack

# Recursive, also O(n^2), no second stack needed

# def sort_stack(stack):
#     if (not stack.is_empty()):
#         # Pop the top element off the stack
#         value = stack.pop()
#         # Sort the remaining stack recursively
#         sort_stack(stack)
#         # Push the top element back into the sorted stack 
#         insert(stack, value) 
 
# def insert(stack, value):
#     if (stack.is_empty() or value < stack.peek()):
#         stack.push(value)
#     else:
#         temp = stack.pop()
#         insert(stack, value)
#         stack.push(temp)

def sort_stack(stack):
    if not stack.is_empty():
        value = stack.pop()
        sort_stack(stack)
        insert(stack, value)

def insert(stack, value):
    if (stack.is_empty() or value < stack.peek()):
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)

# O(nlogn) is just pop out into list, sort, pop back into list

# new_stack = MyStack()
# new_stack.push(23)
# new_stack.push(60)
# new_stack.push(12)
# new_stack.push(42)
# new_stack.push(4)
# new_stack.push(92)
# new_stack.push(2)
# output_stack = sort_stack(new_stack)
# for _ in range(output_stack.size()):
#     print(output_stack.pop())

rec_stack = MyStack()
rec_stack.push(23)
rec_stack.push(60)
rec_stack.push(12)
rec_stack.push(42)
rec_stack.push(4)
rec_stack.push(92)
rec_stack.push(2)
sort_stack(rec_stack)
for _ in range(rec_stack.size()):
    print(rec_stack.pop())