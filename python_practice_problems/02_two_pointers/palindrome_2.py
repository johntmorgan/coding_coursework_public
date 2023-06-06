#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:08:22 2023

@author: johnmorgan
"""

def is_palindrome(s):
    skipped = False
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] == s[right - 1] and skipped == False:
            right -= 1
            skipped = True
        elif s[left + 1] == s[right] and skipped == False:
            left += 1
            skipped = True
        else:
            return False
    return True
    
    
s = "madamer"
print(is_palindrome(s))