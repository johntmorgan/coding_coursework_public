#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:51:44 2023

@author: johnmorgan
"""

# O(n^2) brute force

def longest_sub_palindrome(pal_string):
    if len(pal_string) == 0:
        return ""
    elif len(pal_string) == 1:
        return pal_string
    longest, long_pal = 0, ""
    for index, letter in enumerate(pal_string):
        for co_index in range(index, len(pal_string)):
            if pal_string[co_index] == letter:
                start = index
                end = co_index
                length = 2
                valid = True
                while start < end:
                    start += 1
                    end -= 1
                    if pal_string[start] == pal_string[end]:
                        if start == end:
                            length += 1
                        elif start < end:
                            length += 2
                    else:
                        valid = False
                if valid == True and length > longest:
                    longest = length
                    long_pal = pal_string[index:index + longest]
    return long_pal

# def longest_sub_palindrome(pal_string):
#     res = ""
#     for i in range(len(pal_string)):
#         res = max(helper(pal_string, i, i), helper(pal_string, i, i + 1), res, key=len)
#     return res
   
    
# def helper(s,l,r):
#     while 0 <= l and r < len(s) and s[l] == s[r]:
#             l -= 1; r += 1 
#     return s[l+1:r]

pal_str = "babad"
print(longest_sub_palindrome(pal_str))
pal_str = "abcdefghgfe"
print(longest_sub_palindrome(pal_str))
pal_str = "aabbccddccbbae"
print(longest_sub_palindrome(pal_str))