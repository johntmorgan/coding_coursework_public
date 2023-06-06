#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:55:10 2023

@author: johnmorgan
"""

def rpn(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            second = stack.pop()
            first = stack.pop()
            if token == "+":
                stack.append(first + second)
            elif token == "-":
                stack.append(first - second)
            elif token == "*":
                stack.append(first * second)
            else:
                stack.append(first // second)
        else:
            stack.append(int(token))
    return stack.pop()
    
    
    
tokens = ["2","1","+","3","*"]
print(rpn(tokens))