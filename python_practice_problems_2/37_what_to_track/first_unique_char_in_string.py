#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:31:15 2023

@author: johnmorgan
"""

# O(n) time where n is number of chars
# O(1) space, limited number of chars to store

def first_unique_char(s):
    freq = {}
    for char in s:
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1
    for index, char in enumerate(s):
        if freq[char] == 1:
            return index
    return -1


s = "baefeab"
print(first_unique_char(s))