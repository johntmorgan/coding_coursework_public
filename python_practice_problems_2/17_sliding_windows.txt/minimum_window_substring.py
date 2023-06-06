#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:32:05 2023

@author: johnmorgan
"""

# Compared to subsequence, order of characters does not matter here

# Brute force:
# Monitor if all components have appeared in substring
# Go down string until all chars included
# Do the same thing from each char
# O(n^2)

# Goood
# O(n + m) sliding window solution
# O(n + m) space complexity due to hash maps created

def min_window(s, t):
    r_count = dict()
    window = dict()
    result, result_len = "", float('inf')
    for char in t:
        if char in r_count.keys():
            r_count[char] = r_count[char] + 1
        else:
            r_count[char] = 1
    current = 0
    required = len(r_count)
    start_index = 0
    for index in range(len(s)):
        char = s[index]
        if char in window.keys():
            window[char] = window[char] + 1
        else:
            window[char] = 1
        if char in r_count.keys() and window[char] == r_count[char]:
            current += 1
        if current == required:
            popping = True
            while popping:
                if window[s[start_index]] == 1 and s[start_index] not in r_count:
                    window.pop(s[start_index])
                    start_index += 1
                elif window[s[start_index]] > 1 and s[start_index] not in r_count:
                    window[s[start_index]] = window[s[start_index]] - 1
                    start_index += 1
                elif window[s[start_index]] > 1 and s[start_index] in r_count and \
                    r_count[s[start_index]] < window[s[start_index]]:
                    window[s[start_index]] = window[s[start_index]] - 1
                    start_index += 1
                else:
                    popping = False
            if index + 1 - start_index <= result_len:
                result = s[start_index:index + 1]
                result_len = index - start_index
    return result
            
                
            
    

# s, t = "ABCD" , "ABC"
# print(min_window(s, t))
# s, t = "XYZYX" , "XYZ"
# print(min_window(s, t))
# s, t = "ABXYZJKLSNFC" , "ABC"
# print(min_window(s, t))
# s, t = "AAAAAAAAAAA" , "A"
# print(min_window(s, t))
s, t = "ABDFGDCKAB" , "ABCD"
print(min_window(s, t))