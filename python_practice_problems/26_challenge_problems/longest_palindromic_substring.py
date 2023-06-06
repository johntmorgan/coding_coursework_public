#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:38:32 2023

@author: johnmorgan
"""

def longest_sub_palindrome(pal_string):
    longest = 1
    result = pal_string[0]
    for i, letter in enumerate(pal_string):
        if i < len(pal_string) - 1 and pal_string[i + 1] == letter and (\
            i == 0 or pal_string[i - 1] != letter):
            left, right, curr_len = i, i + 1, 2
        else:
            left, right, curr_len = i, i, 1
        while left > -1 and right < len(pal_string) and \
            pal_string[left] == pal_string[right]:
            if curr_len > longest:
                longest = curr_len
                result = pal_string[left:right + 1]
            left -= 1
            right += 1
            curr_len += 2
    return result
    

print(longest_sub_palindrome("abcdefghgfe"))