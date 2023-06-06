#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:45:11 2023

@author: johnmorgan
"""

# Recursive but inefficient, no memo

from collections import defaultdict

def recurse_word_break(pre, suf, word_dict, result):
    if suf == "":
        result.append(pre.strip() + " " + suf)
        return
    for wds in word_dict:
        if suf[0:len(wds)] == wds:
            recurse_word_break(pre + " " +  wds, suf[len(wds):], word_dict, result)

def word_break(s, word_dict):
    result = []
    recurse_word_break("", s, word_dict, result)
    return result

# Memo pattern - review
# O(n * k + 2^n) O(n) subproblems where n = number letters, O(k) = length of dictionary
# O(2^n) to construct memo in worst case - can store that many
# O(n * 2^n + k) space where n is number of letters

def word_break(s, word_dict):
    memo = {}
    return helper(s, set(word_dict), memo)

def helper(s, dictionary, memo):
    if not s:
        return []
    if s in memo:
        return memo[s]
    res = []
    for word in dictionary:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(s)
        else:
            result_of_the_rest = helper(s[len(word):], dictionary, memo)
            res += [word + ' ' + item for item in result_of_the_rest]
    memo[s] = res
    return res

s = "magiclly"
word_dict = ["ag","al","icl","mag","magic","ly","lly"]
print(word_break(s, word_dict))

s = "raincoats" 
word_dict = ["rain", "oats", "coat", "s", "rains", "oat", "coats", "c"]
print(word_break(s, word_dict))