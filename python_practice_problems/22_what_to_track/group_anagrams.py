#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:43:20 2023

@author: johnmorgan
"""

# O(n * k) - word * letters/word

def group_anagrams(strs):
    str_dict = {}
    for astr in strs:
        chrs = [0] * 26
        for letter in astr:
            val = ord(letter) - 97
            chrs[val] += 1
        for index in range(len(chrs)):
            chrs[index] = str(chrs[index])
        key = "".join(chrs)
        if key in str_dict:
            str_dict[key] += [astr]
        else:
            str_dict[key] = [astr]
    result = []
    for key in str_dict:
        result.append(str_dict[key])
    return result