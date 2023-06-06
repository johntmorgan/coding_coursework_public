#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:44:16 2023

@author: johnmorgan
"""

def min_remove_parentheses(s):
    stack = []
    for index, char in enumerate(s):
        if char == "(":
            stack.append([char, index])
        elif char == ")":
            if len(stack) > 0 and stack[len(stack) - 1][0] == "(":
                stack.pop()
            else:
                stack.append([char, index])
    bad = set()
    for bad_char in stack:
        bad.add(bad_char[1])
    result = ""
    for index, char in enumerate(s):
        if index not in bad:
            result += char
    return result
    
s = ")()r(s(t(q(v)(w(x)y)z())((()("
print(min_remove_parentheses(s))