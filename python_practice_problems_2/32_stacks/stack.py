#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:05:11 2023

@author: johnmorgan
"""

# Creating a stack
def create_stack():
    stack = []
    return stack


# Checking if stack is empty or not
def is_empty(stack):
    return len(stack) == 0


# Push function adds items into the stack
def push(stack, item):
    stack.append(item)
    print("Pushed item: " + str(item))

# Pop function removes an element from the stack
def pop(stack):
    if (is_empty(stack)):
        return "Stack is empty"
    return stack.pop()
