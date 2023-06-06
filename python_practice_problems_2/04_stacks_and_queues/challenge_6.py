#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:56:51 2023

@author: johnmorgan
"""

from MyStack6 import MyStack

# My kludgy but working solution

# def evaluate_post_fix(exp):
#     exp = exp.replace(" ", "")
#     num_stack = MyStack()
#     val_stack = MyStack()
#     operators = ["+", "-", "*", "/"]
#     index = 0
#     while index < len(exp):
#         new_char = exp[index]
#         if new_char.isnumeric():
#             num_stack.push(int(new_char))
#             index += 1
#         elif new_char in operators:
#             if index < len(exp) - 1 and exp[index + 1] in operators:
#                 if new_char == "*":
#                     if exp[index + 1] == "+":
#                         val_stack.push(num_stack.pop() * num_stack.pop())
#                     elif exp[index + 1] == "-":
#                         val_stack.push(-(num_stack.pop() * num_stack.pop()))
#                 elif new_char == "/":
#                     denom = num_stack.pop()
#                     if exp[index + 1] == "+":
#                         val_stack.push(num_stack.pop() / denom)
#                     elif exp[index + 1] == "-":
#                         val_stack.push(-(num_stack.pop() / denom))
#                 index += 2
#             else:
#                 if new_char == "+":
#                     val_stack.push(num_stack.pop())
#                 elif new_char == "-":
#                     val_stack.push(-num_stack.pop())
#                 index += 1
#         else:
#             index += 1
#     while not num_stack.is_empty():
#         val_stack.push(num_stack.pop())
#     value = 0
#     while not val_stack.is_empty():
#         value += val_stack.pop()
#     return value

# The good way to do it
# O(n), go across string once

# def evaluate_post_fix(exp):
#     exp = exp.replace(" ", "")
#     stack = MyStack()
#     try:
#         for char in exp:
#             if char.isdigit():
#                 stack.push(char)
#             else:
#                 right = stack.pop()
#                 left = stack.pop()
#                 ''' Using Python's eval () method that takes a str expression, 
#                 evaluates it and returns an integer '''  
#                 stack.push(str(eval(left + char + right)))
#         return int(float(stack.pop()))
#     except TypeError:
#         return "Invalid Sequence"

def evaluate_post_fix(exp):
    exp = exp.replace(" ", "")
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                stack.push(char)
            else:
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        return(int(float(stack.pop())))
    except TypeError:
        return "Invalid Sequence"

# exp = "6 3 8 * + 4 -"
# print(evaluate_post_fix(exp))
exp = "921 * - 8 - 4 +"
print(evaluate_post_fix(exp))