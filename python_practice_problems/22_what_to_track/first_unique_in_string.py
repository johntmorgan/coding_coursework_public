#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:35:37 2023

@author: johnmorgan
"""

def first_unique_char(s):
    freq = {}
    for letter in s:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    for index, letter in enumerate(s):
        if freq[letter] == 1:
            return index
    return -1