#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:23:06 2023

@author: johnmorgan
"""

# Time O(n * k) - n is list len, k is max str length 
# (Could also be O(m) where m is total number of letters... - JM)
# Space O(n * k) - O(n) dictionary size, max string size k

def group_anagrams(strs):
    hmap = {}
    for astr in strs:
        chrs = [0] * 26
        for letter in astr:
            val = ord(letter) - 97
            chrs[val] += 1
        chr_str = tuple(chrs)
        if chr_str in hmap.keys():
            hmap[chr_str] += [astr]
        else:
            hmap[chr_str] = [astr]
    result = []
    for val in hmap.values():
        result.append(val)
    return result


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))