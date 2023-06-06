#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:27:32 2023

@author: johnmorgan
"""

def longest_palindrome(pal_string):
    hmap = {}
    for letter in pal_string:
        if letter not in hmap:
            hmap[letter] = 1
        else:
            hmap[letter] += 1
    print(hmap)
    result = 0
    odd_result = False
    for key in hmap:
        if hmap[key] % 2 == 0:
            result += hmap[key]
        else:
            result += hmap[key] - 1
            odd_result = True
    if odd_result:
        result += 1
    return result


pal_string = "sfbaisdugfiubasdjFSDIBJS"
print(longest_palindrome(pal_string))