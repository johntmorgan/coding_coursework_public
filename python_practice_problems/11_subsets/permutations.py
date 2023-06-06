#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:29:11 2023

@author: johnmorgan
"""

# Review - first answer resulted in overflow
# O(n!) time complexity
# O(n) space - depth of call stack

def recurse_word(result, added, left):
    if len(left) == 0:
        result.append(added)
    else:
        for index in range(len(left)):
            recurse_word(result, added + left[index], left[:index] + left[index + 1:])
        
def permute_word(word):
    result = []
    recurse_word(result, "", word)
    return result
    
    
word = "idk"
print(permute_word(word))