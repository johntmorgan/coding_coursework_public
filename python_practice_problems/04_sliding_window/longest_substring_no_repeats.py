#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:53:38 2023

@author: johnmorgan
"""

def find_longest_substring(input_string):
    window = set()
    start, end = 0, 0
    max_len = 0
    output = ""
    while end < len(input_string):
        letter = input_string[end]
        if letter not in window:
            window.add(input_string[end])
        else:
            while input_string[start] != letter:
                if input_string[start] in window:
                    window.remove(input_string[start])
                start += 1
            start += 1
        length = end - start + 1
        if length > max_len:
            max_len = length
            output = input_string[start:end + 1]
        end += 1
    return output

def find_longest_substring(input_string):
    window = set()
    output = ""
    return output

input_string = "abcdbea"
print(find_longest_substring(input_string))

input_string = "aba"
print(find_longest_substring(input_string))

input_string = "abccabcabcc"
print(find_longest_substring(input_string))

input_string = "aaaabaaa"
print(find_longest_substring(input_string))

input_string = "bbbbb"
print(find_longest_substring(input_string))