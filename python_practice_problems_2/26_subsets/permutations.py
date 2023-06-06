#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:09:37 2023

@author: johnmorgan
"""

# O(n!) time complexity
# O(n) space complexity - depends on depth of call stack

def recurse_word(pre, post, result):
    if len(post) == 0:
        result.append(pre)
        return
    else:
        for index in range(len(post)):
            recurse_word(pre + post[index], post[:index] + post[index + 1:], result)
        
def permute_word(word):
    result = []
    recurse_word("", word, result)
    return result


print(permute_word("abc"))
# print(permute_word("abcd"))