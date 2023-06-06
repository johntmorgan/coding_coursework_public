#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:18:44 2023

@author: johnmorgan
"""

# Brute force JM

# def fsi_recursive(m, n, p, i, j):
#     if i + j == len(p):
#         if i == len(m) - 1 and j == len(n) - 1:
#             return True
#         else:
#             return False
#     if i == len(m):
#         return n[j:] == p[i + j:] 
#     if j == len(n):
#         return m[:i] == p[i + j:]
#     if m[i] == p[i + j]:
#         if n[j] == p[i + j]:
#             return fsi_recursive(m, n, p, i + 1, j) or fsi_recursive(m, n, p, i, j + 1)
#         else:
#             return fsi_recursive(m, n, p, i + 1, j)
#     elif n[j] == p[i + j]:
#         return fsi_recursive(m, n, p, i, j + 1)
#     else:
#         return False

# def find_strings_interleaving(m, n, p):
#     i, j = 0, 0
#     return fsi_recursive(m, n, p, i, j)

# Tighter brute force, improving JM code from solution
# Time complexity O(2^(m + n))

def fsi_recursive(m, n, p, i, j, k):
    if k == len(p) and i == len(m) and j == len(n):
        return True
    if k == len(p):
        return False
    b1 = False
    b2 = False
    if i < len(m) and m[i] == p[k]:
        b1 = fsi_recursive(m, n, p, i + 1, j, k + 1)
    if j < len(n) and n[j] == p[k]:
        b2 = fsi_recursive(m, n, p, i, j + 1, k + 1)
    return b1 or b2

def find_strings_interleaving(m, n, p):
    return fsi_recursive(m, n, p, 0, 0, 0)

# Tabularization
# O(mn)

def find_strings_interleaving(m, n, p):
    lookup_table = [[False for i in range(len(n) + 1)] for i in range(len(m) + 1)]
    if len(m) + len(n) != len(p):
        return False
    for m_index in range(len(m) + 1):
        for n_index in range(len(n) + 1):
            if m_index == 0 and n_index == 0:
                lookup_table[m_index][n_index] = True
            elif m_index == 0 and n[n_index - 1] == p[m_index + n_index - 1]:
                lookup_table[m_index][n_index] = lookup_table[m_index][n_index - 1]
            elif n_index == 0 and m[m_index - 1] == p[m_index + n_index - 1]:
                lookup_table[m_index][n_index] = lookup_table[m_index - 1][n_index]
            else:
                if m_index > 0 and m[m_index - 1] == p[m_index + n_index - 1]:
                    lookup_table[m_index][n_index] = lookup_table[m_index - 1][n_index]
                if n_index > 0 and n[n_index - 1] == p[m_index + n_index - 1]:
                    lookup_table[m_index][n_index] |= lookup_table[m_index][n_index - 1]
    return lookup_table[len(m)][len(n)]

m = "abd"
n = "cef"
p = "abcdef"
print(find_strings_interleaving(m, n, p))

m = "abd"
n = "cef"
p = "abcdfe"
print(find_strings_interleaving(m, n, p))

m = "www.educative.io/explore"
n = "educative.io/edpresso"
p = "educative.io"
print(find_strings_interleaving(m, n, p))