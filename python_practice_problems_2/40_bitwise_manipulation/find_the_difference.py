#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:41:42 2023

@author: johnmorgan
"""

# Review

# O(n) time complexity - n is length of string
# O(1) space, do not use extra space

def extra_character_index(str1, str2):

    result = 0
    len1 = len(str1)
    len2 = len(str2)

    for i in range(len1):
        result = result ^ (ord)(str1[i])

    for j in range(len2):
        result = result ^ (ord)(str2[j])

    if len(str1) > len(str2):
        index = str1.index((chr)(result))
        return index
    else:
        index = str2.index((chr)(result))
        return index

# Multiplication version for fun
def extra_character_index(str1, str2):

    result = 1
    len1 = len(str1)
    len2 = len(str2)

    for i in range(len1):
        result = result * (ord)(str1[i])
        
    for j in range(len2):
        result = result / (ord)(str2[j])

    if len1 > len2:
        result = int(result)
        index = str1.index((chr)(result))
        return index
    else:
        result = int(1/result)
        index = str2.index((chr)(result))
        return index


str1, str2 = "wxyz", "zwxgy"
print(extra_character_index(str1, str2))