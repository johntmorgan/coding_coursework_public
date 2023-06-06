#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:17:26 2023

@author: johnmorgan
"""

# Can also multiply by first set of letters, divide by second

def find_the_difference(str1, str2):
    result = 0
    for letter in str1:
        result = result ^ ord(letter)
    for letter in str2:
        result = result ^ ord(letter)
    letter = chr(result)
    if len(str1) > len(str2):
        return str1.index(letter)
    else:
        return str2.index(letter)
    return -1

def find_the_difference(str1, str2):
    for index in range(max(len(str1), len(str2))):
        if index > len(str1) - 1 or index > len(str2) - 1:
            return index
        if str1[index] != str2[index]:
            return index
    return -1


print(find_the_difference("loved", "love"))
