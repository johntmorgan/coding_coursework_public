#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:14:36 2023

@author: johnmorgan
"""

# O(k^n * n)
# O(n * k) space

def recurse_combo(used, unused, result, d):
    if len(unused) == 0:
        result.append(used)
        return
    else:
        letters = d[int(unused[0])]
        for letter in letters:
            recurse_combo(used + letter, unused[1:], result, d)
            
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
    recurse_combo("", digits, result, d)
    return result

ch_str = "23"
print(letter_combinations(ch_str))