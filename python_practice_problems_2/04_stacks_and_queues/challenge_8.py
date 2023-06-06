#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:18:44 2023

@author: johnmorgan
"""

from MyStack6 import MyStack

# O(n) time

def is_balanced(str):
    stack = MyStack()
    for paren in str:
        if paren in ["(", "{", "["]:
            stack.push(paren)
        elif paren == ")":
            if stack.pop() != "(":
                return False
        elif paren == "}":
            if stack.pop() != "{":
                return False
        elif paren == "]":
            if stack.pop() != "[":
                return False
        else:
            return False
    if stack.size() > 0:
        return False
    return True


str1 = "{[({})]}"
print(is_balanced(str1))
str2 = "{[({)}]}"
print(is_balanced(str2))