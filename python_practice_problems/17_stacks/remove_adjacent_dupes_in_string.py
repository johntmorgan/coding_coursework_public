#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:12:19 2023

@author: johnmorgan
"""

def remove_duplicates(in_str):
    stack = []
    for char in in_str:
        if len(stack) == 0 or stack[len(stack) - 1] != char:
            stack.append(char)
        else:
            stack.pop()
    return "".join(stack)


in_str = "xyyxxzx"
print(remove_duplicates(in_str))

in_str = "sadyydassa"
print(remove_duplicates(in_str))