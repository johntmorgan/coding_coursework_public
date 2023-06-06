#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:12:11 2023

@author: johnmorgan
"""

# Brute force
# Time complexity O(2^n)
# Space complexity O(n)

def lps_recursive(s, i, j, count):
    if j < i:
        return count
    if i == j:
        return count + 1
    if s[i] == s[j]:
        return lps_recursive(s, i + 1, j - 1, count + 2)
    c1 = lps_recursive(s, i + 1, j, count)
    c2 = lps_recursive(s, i, j - 1, count)
    return max(c1, c2)

def longest_palindromic_subsequence(s):
    i, j, count = 0, len(s) - 1, 0
    return lps_recursive(s, i, j, count)

# O(n^2) - actually got this one w/lookup! - JM
# Space complexity also O(n^2)

def lps_recursive(s, i, j, count, lookup):
    if j < i:
        return count
    if i == j:
        return count + 1
    if lookup[i][j] == 0:
        if s[i] == s[j]:
            lookup[i][j] = lps_recursive(s, i + 1, j - 1, count + 2, lookup)
        else:
            c1 = lps_recursive(s, i + 1, j, count, lookup)
            c2 = lps_recursive(s, i, j - 1, count, lookup)
            lookup[i][j] = max(c1, c2)
    return lookup[i][j]
    
def longest_palindromic_subsequence(s):
    i, j, count = 0, len(s) - 1, 0
    lookup = [[0 for _ in range(len(s))] for _ in range(len(s))]
    return lps_recursive(s, i, j, count, lookup)

# Tabularization
# O(n^2) again

def longest_palindromic_subsequence(s):

    lookup_table = [[0 for x in range(len(s))] for x in range(len(s))]
    for i in range(len(s)):
        lookup_table[i][i] = 1
    for start_index in reversed(range(len(s))):
        for end_index in range(start_index + 1, len(s)):
            # case 1: elements at the beginning and the end are the same
            if s[start_index] == s[end_index]:
                lookup_table[start_index][end_index] = 2 + lookup_table[start_index + 1][end_index - 1]
            else:  # case 2: skip one element either from the beginning or the end
                lookup_table[start_index][end_index] = max(lookup_table[start_index + 1][end_index],
                                                           lookup_table[start_index][end_index - 1])
    return lookup_table[0][len(s) - 1]

s = "abdbca"
print(longest_palindromic_subsequence(s))

s = "abdbcfa"
print(longest_palindromic_subsequence(s))

s = "abbca"
print(longest_palindromic_subsequence(s))