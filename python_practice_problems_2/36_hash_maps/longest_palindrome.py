#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:09:13 2023

@author: johnmorgan
"""

def longest_palindrome(pal_string):
    d = {}
    for letter in pal_string:
        if letter in d.keys():
            d[letter] = d[letter] + 1
        else:
            d[letter] = 1
    len_pal = 0
    odd_found = False
    for key in d.keys():
        if d[key] % 2 == 0:
            len_pal += d[key]
        else:
            if odd_found == False:
                odd_found = True
            len_pal += (d[key] - 1)
    if odd_found:
        len_pal += 1
    return len_pal

# pal = "aagshgsh"
# print(longest_palindrome(pal))
# pal2 = "aagshgsha"
# print(longest_palindrome(pal2))
# pal3 = "aagshgshb"
# print(longest_palindrome(pal3))
pal4 = "asfewgfweoifhsdb"
print(longest_palindrome(pal4))
