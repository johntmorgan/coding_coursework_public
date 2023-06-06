#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 18:10:38 2023

@author: johnmorgan
"""

# Naive approach: consider every possible substring
# Two nested loops to get all substrings
# Loop to check for smallest
# O(n^3), space complexity O(1)

# Good solution
# O(n * m)
# Where m is the length of str2
# Space complexity again O(1)

def min_window(str1, str2):
    min_len, min_subseq = float('inf'), ""
    p1, p2 = 0, 0
    while p1 < len(str1):
        if str1[p1] == str2[p2]:
            if p2 == len(str2) - 1:
                start = p1
                end = p1 + 1
                while p2 >= 0:
                    if str1[start] == str2[p2]:
                        start -= 1
                        p2 -= 1
                    else:
                        start -= 1
                new_len = end - start + 1
                if new_len < min_len:
                    min_len = new_len
                    min_subseq = str1[start + 1:end]
                p2 = 0
            else:
                p1 += 1
                p2 += 1
        else:
            p1 += 1
    return min_subseq
    
    
str1, str2 = "abcdebdde" , "bde"
print(min_window(str1, str2))
str1, str2 = "fgrqsqsnodwmxzkzxwqegkndaa" , "kzed"
print(min_window(str1, str2))
str1, str2 = "michmznaitnjdnjkdsnmichmznait" , "michmznait"
print(min_window(str1, str2))
str1, str2 = "afgegrwgwga" , "aa"
print(min_window(str1, str2))
str1, str2 = "abababa" , "ba"
print(min_window(str1, str2))
str1, str2 = "cnhczmccqouqadqtmjjzl" , "cm"
print(min_window(str1, str2))