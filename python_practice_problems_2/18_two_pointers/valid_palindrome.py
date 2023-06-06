#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 17:14:53 2023

@author: johnmorgan
"""

# Naive: reverse string, compare
# Linear time complexity, but uses extra space

# Good solution
# O(n) time, O(1) space

def is_palindrome(s):
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    start, end = 0, len(s) - 1
    while end > start:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
          

s = "kayak"
print(is_palindrome(s))
s = "hello"
print(is_palindrome(s))
s = "RACEACAR"
print(is_palindrome(s))
s = "A"
print(is_palindrome(s))
s = "ABCDABCD"
print(is_palindrome(s))
s = "DCBAABCD"
print(is_palindrome(s))
s = "ABCBA"
print(is_palindrome(s))