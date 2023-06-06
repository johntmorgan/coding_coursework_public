#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:02:33 2023

@author: johnmorgan
"""

# O(n) time where n is string length
# O(1) space

def is_isomorphic(string1, string2):
    if len(string1) != len(string2):
        return False
    hmap1, hmap2 = {}, {}
    for index, letter in enumerate(string1):
        if letter not in hmap1.keys():
            hmap1[letter] = string2[index]
        else:
            if hmap1[letter] != string2[index]:
                return False
        if string2[index] not in hmap2.keys():
            hmap2[string2[index]] = letter
        else:
            if hmap2[string2[index]] != letter:
                return False
    return True
        
        


print(is_isomorphic("egg", "all"))
print(is_isomorphic("foo", "bar"))