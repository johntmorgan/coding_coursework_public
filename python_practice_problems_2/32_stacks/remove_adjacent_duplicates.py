#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 17:29:49 2023

@author: johnmorgan
"""

# O(n) time complexity
# O(n) space complexity

def remove_duplicates(string):
    stack = []
    for char in string:
        if stack == []:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    return "".join(stack)


string = "abbddaccaaabcd"
print(remove_duplicates(string))