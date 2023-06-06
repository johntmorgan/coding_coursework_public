#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:46:05 2023

@author: johnmorgan
"""

# JM brute force - works
# Exponential time complexity

# def me_recur(s1, s2, i, j, count, moves):
#     if i == len(s1) and j == len(s2):
#         if count < 4:
#             print(count, moves)
#         return count
#     if i == len(s1):
#         return float('inf')
#     if j == len(s2):
#         return float('inf')
#     else:
#         if s1[i] == s2[j]:
#             return me_recur(s1, s2, i + 1, j + 1, count, moves + ['match'])
#         else:
#             subst = me_recur(s1, s2, i + 1, j + 1, count + 1, moves + ['subst'])
#             rem1 = me_recur(s1, s2, i + 1, j, count + 1, moves + ['advance s1'])
#             rem2 = me_recur(s1, s2, i, j + 1, count + 1, moves + ['advance s2'])
#             return min(subst, rem1, rem2)
    
# def min_edit_dist(str1, str2):
#     return me_recur(str1, str2, 0, 0, 0, [])

def me_recur(s1, s2, lookup, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if lookup[i - 1][j -  1] != -1:
        return lookup[i - 1][j - 1]
    if s1[i - 1] == s2[j - 1]:
        lookup[i - 1][j - 1] = me_recur(s1, s2, lookup, i - 1, j - 1)
        return lookup[i - 1][j - 1]
    subst = me_recur(s1, s2, lookup, i - 1, j - 1)
    rem1 = me_recur(s1, s2, lookup, i - 1, j)
    rem2 = me_recur(s1, s2, lookup, i, j - 1)
    lookup[i - 1][j - 1] = 1 + min(subst, rem1, rem2)
    return lookup[i - 1][j - 1]
    
def min_edit_dist(str1, str2):
    lookup = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]
    return me_recur(str1, str2, lookup, len(str1), len(str2))

# Tabularization

def min_edit_dist_recursive(str1, str2, m, n):
    lookup_table = [[-1 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                lookup_table[i][j] = j
            elif j == 0:
                lookup_table[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                lookup_table[i][j] = lookup_table[i - 1][j - 1]
            else:
                lookup_table[i][j] = 1 + min(lookup_table[i][j - 1],  # Insert
                                             lookup_table[i - 1][j],  # Remove
                                             lookup_table[i - 1][j - 1])  # Replace
    return lookup_table[m][n]

def min_edit_dist(str1, str2):
    return min_edit_dist_recursive(str1, str2, len(str1), len(str2))

str1 = "sunday"
str2 = "saturday"
print(min_edit_dist(str1, str2))