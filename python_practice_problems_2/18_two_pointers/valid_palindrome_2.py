#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:05:07 2023

@author: johnmorgan
"""

def is_palindrome(s):
    start, end = 0, len(s) - 1
    skips = 0
    while end > start and skips <= 1:
        if s[end] == s[start]:
            start += 1
            end -= 1
        elif s[end - 1] == s[start]:
            end -= 1
            skips += 1
        elif s[start + 1] == s[end]:
            start += 1
            skips += 1
        else:
            return False
    if skips <= 1:
        return True
    return False

pal = "madame"
print(is_palindrome(pal))
pal = "dead"
print(is_palindrome(pal))
pal = "abca"
print(is_palindrome(pal))
pal = "tebbem"
print(is_palindrome(pal))
pal = "eeccccbebaeeabebccceea"
print(is_palindrome(pal))
pal = "ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno"
print(is_palindrome(pal))