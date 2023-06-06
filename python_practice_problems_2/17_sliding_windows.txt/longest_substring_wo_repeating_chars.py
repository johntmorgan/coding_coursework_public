#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:32:16 2023

@author: johnmorgan
"""

# Review when brain not addled by anti-allergy/immune meds

def find_longest_substring(input_string):
    if len(input_string) == 0:
        return 0
    n = len(input_string)
    st_curr, longest, len_curr, start = 0, 0, 0, 0
    last_seen_at = {}
    for index, val in enumerate(input_string):
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            if last_seen_at[val] >= st_curr:
                len_curr = index - st_curr
                if longest < len_curr:
                    longest = len_curr
                    start = st_curr
                st_curr = last_seen_at[val] + 1
            last_seen_at[val] = index
    index += 1
    if longest < index - st_curr:
        start = st_curr
        longest = n - st_curr
    return longest

s = "abcdbea"
print(find_longest_substring(s))
s = "aba"
print(find_longest_substring(s))
s = "abccabcabcc"
print(find_longest_substring(s))
# s = "aaaabaaa"
# print(find_longest_substring(s))
# s = "bbbbb"
# print(find_longest_substring(s))