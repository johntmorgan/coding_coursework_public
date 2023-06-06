#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:25:08 2023

@author: johnmorgan
"""

# Review
# O(n * m) - n is number of chars in s1, m in s2
# Space O(1)

def min_window(str1, str2):
    p1, p2 = 0, 0
    min_length = float('inf')
    subseq = ""
    while p1 < len(str1):
        if str1[p1] == str2[p2]:
            p1 += 1
            p2 += 1
            if p2 == len(str2):
                start = p1 - 1
                end = p1
                p2 -= 1
                while p2 >= 0:
                    if str1[start] == str2[p2]:
                        start -= 1
                        p2 -= 1
                    else:
                        start -= 1
                start += 1
                length = end - start
                if length < min_length:
                    min_length = length
                    subseq = str1[start:end]
                p1, p2 = start + 1, 0
        else:
            p1 += 1
    return subseq
    

str1 = "abcdebdde"
str2 = "bde"
print(min_window(str1, str2))