#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:32:50 2023

@author: johnmorgan
"""

# Review

import stack as s

def insertAtBottom(stack, item):
    if s.isEmpty(stack):
        s.push(stack, item)
    
    else:
        temp = s.pop(stack)
        insertAtBottom(stack, item)
        s.push(stack, temp)

def reverse(testVariable):
    if not s.isEmpty(testVariable):
        temp = s.pop(testVariable)
        reverse(testVariable)
        insertAtBottom(testVariable, temp)
    
stack = s.createStack()
s.push(stack, 2)
s.push(stack, 3)
s.push(stack, 5)
s.push(stack, 8)
print(stack)
reverse(stack)
print(stack)