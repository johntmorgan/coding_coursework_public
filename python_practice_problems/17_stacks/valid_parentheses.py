#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:35:56 2023

@author: johnmorgan
"""

def is_valid(string):
    stack = []
    for char in string:
        if char in ["(", "[", "{"]:
            stack.append(char)
        elif len(stack) > 0:
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0
                


string = "{}[]{}[{}]"
print(is_valid(string))
string = "{}[]{}[{}])"
print(is_valid(string))
string = "{}[]()[{}]"
print(is_valid(string))


