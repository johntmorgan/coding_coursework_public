#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 19:08:39 2023

@author: johnmorgan
"""

def find_anagrams(a, b):
    if len(a) < len(b):
        return []
    bdict = {}
    for letter in b:
        if letter in bdict:
            bdict[letter] += 1
        else:
            bdict[letter] = 1
    result = []
    adict = {}
    for index in range(len(b)):
        letter = a[index]
        if letter in adict:
            adict[letter] += 1
        else:
            adict[letter] = 1
    for index in range(len(a) - len(b) + 1):
        if adict == bdict:
            result.append(index)
        leaving_letter = a[index]
        if adict[leaving_letter] == 1:
            del adict[leaving_letter]
        else:
            adict[leaving_letter] -= 1
        if index + len(b) < len(a):
            letter = a[index + len(b)]
            if letter in adict:
                adict[letter] += 1
            else:
                adict[letter] = 1
    return result

a = "abab"
b = "ab"
print(find_anagrams(a, b))

a = "cbaebabacd"
b = "abc"
print(find_anagrams(a, b))