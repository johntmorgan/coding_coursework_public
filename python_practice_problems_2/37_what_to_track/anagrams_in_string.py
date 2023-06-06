#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:35:51 2023

@author: johnmorgan
"""

# O(n + m) time, n = # chars in string 1, m = number of chars in string 2
# O(n + m) space - hash maps

def find_anagrams(a, b):
    if len(b) > len(a):
        return []
    bdict = {}
    for letter in b:
        if letter in bdict.keys():
            bdict[letter] += 1
        else:
            bdict[letter] = 1
    result = []
    adict = {}
    index = 0
    while index < len(a):
        if index >= len(b):
            if adict[a[index - len(b)]] > 1:
                adict[a[index - len(b)]] -= 1
            else:
                del adict[a[index - len(b)]]
            letter = a[index]
            if letter in adict.keys():
                adict[letter] += 1
            else:
                adict[letter] = 1
            if adict == bdict:
                result += [index - len(b) + 1]
            index += 1
        else:
            while index < len(b):
                letter = a[index]
                if letter in adict.keys():
                    adict[letter] += 1
                else:
                    adict[letter] = 1
                index += 1
            if adict == bdict:
                result += [0]
    return result

a = "abab"
b = "ab"
print(find_anagrams(a, b))

a = "cbaebabacd" 
b = "abc"
print(find_anagrams(a, b))