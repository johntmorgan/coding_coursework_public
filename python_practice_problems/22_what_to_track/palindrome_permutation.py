#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:11:57 2023

@author: johnmorgan
"""

# Average O(n), worst_case O(n^2)
# Space O(1) - bounded by characters

def permute_palindrome(string):
    pal_dict = {}
    for letter in string:
        if letter in pal_dict:
            pal_dict[letter] += 1
        else:
            pal_dict[letter] = 1
    odd_count = 0
    for key in pal_dict:
        if pal_dict[key] % 2 != 0:
            odd_count += 1
    return odd_count <= 1