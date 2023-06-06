#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:54:50 2023

@author: johnmorgan
"""

from MyStack6 import MyStack

# O(n^2) - my brute force solution
# Of course you can just brute force iterate over list, but banned by problem

# def next_greater_element(lst):
#     nge = []
#     stack = MyStack()
#     temp_stack = MyStack()
#     for idx in range(len(lst) - 1, -1, -1):
#         stack.push(lst[(idx)])
#     for elem in lst:
#         stack.pop()
#         while not stack.is_empty() and stack.peek() <= elem:
#             temp_stack.push(stack.pop())
#         if stack.size() > 0:
#             nge.append(stack.peek())
#         else:
#             nge.append(-1)
#         while not temp_stack.is_empty():
#             stack.push(temp_stack.pop())
#     return nge

# O(n)

def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])
    return res

lst = [4, 6, 3, 2, 8, 1]
print(next_greater_element(lst))
