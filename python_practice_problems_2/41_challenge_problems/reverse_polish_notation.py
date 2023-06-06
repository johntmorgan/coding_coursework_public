#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 10:53:19 2023

@author: johnmorgan
"""

def rpn(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "/", "*"]:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == "+":
                stack.append(val2 + val1)
            elif token == "-":
                stack.append(val2 - val1)
            elif token == "*":
                stack.append(val2 * val1)
            elif token == "/":
                stack.append(int(val2 / val1))
        else:
            stack.append(int(token))
    return stack[-1]


tokens = ["2","1","+","3","*"]
print(rpn(tokens))
tokens = ["2", "5", "*", "4", "+", "3", "2", "*", "1", "+", "/"]
print(rpn(tokens))
tokens = ["4","13","5","/","+"]
print(rpn(tokens))
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(rpn(tokens))