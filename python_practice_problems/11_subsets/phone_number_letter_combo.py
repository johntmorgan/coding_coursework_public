#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:55:56 2023

@author: johnmorgan
"""

def recurse_combo(result, d, curr, left):
    if left == "":
        result.append(curr)
    else:
        number = left[0]
        for letter in d[int(number)]:
            recurse_combo(result, d, curr + letter, left[1:])

def letter_combinations(digits):
    d = {}
    d[1] = []
    d[2] = ["a", "b", "c"]
    d[3] = ["d", "e", "f"]
    d[4] = ["g", "h", "i"]
    d[5] = ["j", "k", "l"]
    d[6] = ["m", "n", "o"]
    d[7] = ["p", "q", "r", "s"]
    d[8] = ["t", "u", "v"]
    d[9] = ["w", "x", "y", "z"]
    result = []
    recurse_combo(result, d, "", digits)
    return result
    
    
digits = "73"
print(letter_combinations(digits))