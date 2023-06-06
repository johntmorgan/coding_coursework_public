#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:56:53 2023

@author: johnmorgan
"""

# O(n^2 + 2^n + nl)
# Recursive calls to helper O(n^2), n is query length
# Helper iterates over all possible solutions O(2^n)
# Helper iterates over entire dictionary O(nl), l is length of dict list

# Space O((n * 2^n) + l)

# Review

def rec_word_break(s, word_dict, result):
    if len(s) == 0:
        return
    if s in result:
        return result[s]
    res = []
    for word in word_dict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(s)
        else:
            suffix = rec_word_break(s[len(word):], word_dict, result)
            for item in suffix:
                item = word + " " + item
                res.append(item)
    result[s] = res
    return res

def word_break(s, word_dict):
    result = {}
    output = rec_word_break(s, word_dict, result)
    print(result)
    return output

s = "magiclly"
word_dict = ["ag","al","icl","mag","magic","ly","lly"]
print(word_break(s, word_dict))