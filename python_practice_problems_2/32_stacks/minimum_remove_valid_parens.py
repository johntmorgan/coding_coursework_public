#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:37:56 2023

@author: johnmorgan
"""

# O(n) time and space

def min_remove_parentheses(s):
    stack = []
    for index in range(len(s)):
        char = s[index]
        if char == "(":
            stack.append(["(", index])
        elif char == ")":
            if len(stack) > 0 and stack[-1][0] == "(":
                stack.pop()
            else:
                stack.append([")", index])
    bad_indices = []
    for elem in stack:
        bad_indices.append(elem[1])
    output = ""
    for index in range(len(s)):
        if index not in bad_indices:
            output += s[index]
    return output
    
s = "ab)ca(so)(sc(s)("
print(min_remove_parentheses(s))