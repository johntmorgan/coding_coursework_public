#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:04:02 2023

@author: johnmorgan
"""

# Brute force, awful
# O(2^(n + m))

def lcs_recursion(s1, s2, i, j, count):
    if i == len(s1) or j == len(s2):
        return count
    if s1[i] == s2[j]:
        count = lcs_recursion(s1, s2, i + 1, j + 1, count + 1)
    c1 = lcs_recursion(s1, s2, i + 1, j, 0)
    c2 = lcs_recursion(s1, s2, i, j + 1, 0)
    return max(count, max(c1, c2))
            
def longest_common_substr_length(s1, s2):
    return lcs_recursion(s1, s2, 0, 0, 0)

# Memoization - copied and rewritten for learning
# O(len(s1) * len(s2) * count) - that many subproblems, O(1) for each

def lcs_recursion(lookup_table, s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count
    if lookup_table[i1][i2][count] == -10:
        c1 = count
        if s1[i1] == s2[i2]:
            c1 = lcs_recursion(lookup_table, s1, s2, i1 + 1, i2 + 1, count + 1)
        c2 = lcs_recursion(lookup_table, s1, s2, i1, i2 + 1, 0)
        c3 = lcs_recursion(lookup_table, s1, s2, i1 + 1, i2, 0)
        lookup_table[i1][i2][count] = max(c1, max(c2, c3))
    return lookup_table[i1][i2][count]

def longest_common_substr_length(s1, s2):
    # Declaring a lookup table with dimensions: lookup_table[len(s1)][len(s2)][max_length]
    max_length = max(len(s1), len(s2))
    lookup_table = [[[-10 for k in range(len(s1))] for j in range(len(s2))] for i in range(max_length)]
    return lcs_recursion(lookup_table, s1, s2, 0, 0, 0)

# Tabulation
# O(m * n) complexity

def longest_common_substr_length(s1, s2):
    # Initializing all values in lookup_table to zero
    lookup_table = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    max_length = 0
    for i in range(len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lookup_table[i][j] = 1 + lookup_table[i - 1][j - 1]
                max_length = max(max_length, lookup_table[i][j])
    return max_length

S1 = "0abc321"
S2 = "123abcdef"
print(longest_common_substr_length(S1, S2))

s1 = "www.educative.io/explore"
s2 = "educative.io/edpresso"

print(longest_common_substr_length(s1, s2))