#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:38:30 2023

@author: johnmorgan
"""

def is_valid(string):
    stack= []
    for paren in string:
        if paren in ["(", "[", "{"]:
            stack.append(paren)
        elif len(stack) > 0:
            if paren == ")" and stack[-1] == "(":
                stack.pop()
            elif paren == "]" and stack[-1] == "[":
                stack.pop()
            elif paren == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack) > 0:
        return False
    return True

pstring = "{}[]{}[{}]"
print(is_valid(pstring))
pstring = "{}[]{}[{}])"
print(is_valid(pstring))