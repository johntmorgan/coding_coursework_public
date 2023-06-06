#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:48:25 2023

@author: johnmorgan
"""

from populating_hashmap import *

# Naive: compute string permutations O(n!) time & space
# O(n) average, O(n^2) worst case first part
# O(n) average, O(n^2) worst case second part (really? worst = spread tho - JM)
# O(1) space - bounded number of chars that can be added

def permute_palindrome(st):
    hmap = {}
    for letter in st:
        if letter in hmap.keys():
            hmap[letter] += 1
        else:
            hmap[letter] = 1
    odd_count = 0
    for val in hmap.values():
        if val % 2 != 0:
            odd_count += 1
    return odd_count < 2


print(permute_palindrome("abab"))
print(permute_palindrome("peas"))