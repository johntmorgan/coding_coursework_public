#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:20:57 2023

@author: johnmorgan
"""

def is_isomorphic(string1, string2):
    if len(string1) != len(string2):
        return False
    hmap = {}
    s2used = set()
    for index, letter in enumerate(string1):
        if letter not in hmap:
            hmap[letter] = string2[index]
            if string2[index] in s2used:
                return False
            else:
                s2used.add(string2[index])
        else:
            if hmap[letter] != string2[index]:
                return False
    return True


string1 = "badc"
string2 = "baba"
print(is_isomorphic(string1, string2))