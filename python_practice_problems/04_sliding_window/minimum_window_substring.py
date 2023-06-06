#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:28:36 2023

@author: johnmorgan
"""

from collections import defaultdict

def min_window(s, t):
    window, t_freq = defaultdict(int), defaultdict(int)
    min_len = float('inf')
    output = ""
    for letter in t:
        t_freq[letter] += 1
    start = 0
    for end in range(len(s)):
        if letter in t_freq:
            window[s[end]] += 1
            valid = True
            for compare_letter in t_freq:
                if compare_letter not in window:
                    valid = False
                elif window[compare_letter] < t_freq[compare_letter]:
                    valid = False
            if valid:
                move_window_left = True
                while move_window_left:
                    if s[start] in t_freq and window[s[start]] > t_freq[s[start]]:
                        window[s[start]] -= 1
                        start += 1
                    elif s[start] not in t_freq:
                        start += 1
                    else:
                        move_window_left = False
                length = end - start + 1
                if length < min_len:
                    output = s[start:end + 1]
                    min_len = length
    return output

# GPT

# from collections import defaultdict

# def min_window(s, t):
#     window = defaultdict(int)
#     t_freq = defaultdict(int)
#     for letter in t:
#         t_freq[letter] += 1
#     min_len = float('inf')
#     output = None
#     start = 0
#     for end in range(len(s)):
#         window[s[end]] += 1
#         while all(window[char] >= t_freq[char] for char in t):
#             length = end - start + 1
#             if length < min_len:
#                 output = s[start:end + 1]
#                 min_len = length
#             window[s[start]] -= 1
#             start += 1
#     return output

s = "ABCD"
t = "ABC"
print(min_window(s, t))

s = "XYZYX"
t = "XYZ"
print(min_window(s, t))

s = "ABXYZJKLSNFC"
t = "ABC"
print(min_window(s, t))

s = "AAAAAAAAAAA"
t = "A"
print(min_window(s, t))

s = "ABDFGDCKAB"
t = "ABC"
print(min_window(s, t))