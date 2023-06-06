#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:39:32 2023

@author: johnmorgan
"""

# Brute force
# Time complexity O(2^(n + m))
# Space complexity O(n + m) - recursion stack

def scs_recursive(s1, s2, i, j):
    if i == len(s1):
        return len(s2) - j
    if j == len(s2):
        return len(s1) - i
    if s1[i] == s2[j]:
        return 1 + scs_recursive(s1, s2, i + 1, j + 1)
    length1 = 1 + scs_recursive(s1, s2, i, j + 1)
    length2 = 1 + scs_recursive(s1, s2, i + 1, j)
    return min(length1, length2)

def shortest_common_supersequence(s1, s2):
    i, j = 0, 0
    return scs_recursive(s1, s2, i, j)

# Memoization
# O(mn)
# Just like brute force but with a lookup table

def scs_recursive(lookup_table, s1, s2, i1, i2):
    if i1 == len(s1):
        return len(s2) - i2
    if i2 == len(s2):
        return len(s1) - i1
    if lookup_table[i1][i2] == 0:
        if s1[i1] == s2[i2]:
            lookup_table[i1][i2] = 1 + scs_recursive(lookup_table, s1, s2, i1 + 1, i2 + 1)
        else:
            length1 = 1 + scs_recursive(lookup_table, s1, s2, i1, i2 + 1)
            length2 = 1 + scs_recursive(lookup_table, s1, s2, i1 + 1, i2)
            lookup_table[i1][i2] = min(length1, length2)
    return lookup_table[i1][i2]

def shortest_common_supersequence(s1, s2):
    lookup_table = [[0 for x in range(len(s2))] for x in range(len(s1))]
    return scs_recursive(lookup_table, s1, s2, 0, 0)

# Tabularization
# O(mn)

def shortest_common_supersequence(s1, s2):
    lookup_table = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

    # if one of the strings is of zero length, Shortest common supersequence(SCS)
    # would be equal to the length of the other string
    for i in range(len(s1) + 1):
        lookup_table[i][0] = i

    for j in range(len(s2) + 1):
        lookup_table[0][j] = j
        
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                lookup_table[i][j] = 1 + lookup_table[i - 1][j - 1]
            else:
                lookup_table[i][j] = 1 + min(lookup_table[i - 1][j], lookup_table[i][j - 1])

    return lookup_table[len(s1)][len(s2)]


s1 = "abcf"
s2 = "bdcf"
print(shortest_common_supersequence(s1, s2))

# def shortest_common_supersequence(s1, s2):
#     """
#     Finds a shortest common super sequence length
#     :param s1: First string
#     :param s2: Second string
#     :return: Length of shortest common superstring
#     """
#     return shortest_common_supersequence_recursive(s1, s2, 0, 0)

# # def scs_recursion(lookup_table, s1, s2, i, j, count):
# #     if i == len(s1) or j == len(s2) or count > (len(s1) + len(s2)):
# #         return count
# #     print(i, j, count)
# #     if lookup_table[i][j] > len(s1) + len(s2):
# #         c1 = count
# #         if s1[i] == s2[j]:
# #             c1 = scs_recursion(lookup_table, s1, s2, i + 1, j + 1, count + 1)
# #         if i < len(s1):
# #             c2 = scs_recursion(lookup_table, s1, s2, i + 1, j, count + 1)
# #         else:
# #             c2 = scs_recursion(lookup_table, s1, s2, i, j + 1, count + 1)
# #         if j < len(s2):
# #             c3 = scs_recursion(lookup_table, s1, s2, i, j + 1, count + 1)
# #         else:
# #             c3 = scs_recursion(lookup_table, s1, s2, i + 1, j, count + 1)
# #         lookup_table[i][j] = min(c1, min(c2, c3))
# #     print(lookup_table)
# #     return lookup_table[len(s1)][len(s2)]


# def shortest_common_supersequence(s1, s2):
#     # Declaring a lookup table with dimensions: lookup_table[len(s1)][len(s2)][max_length]
#     max_length = len(s1) + len(s2)
#     lookup_table = [[max_length + 1 for k in range(len(s1) + 1)] for j in range(len(s1) + 1)]
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if i == 0 or j == 0:
#                 lookup_table[i][j] = 1
#             elif s1[i] == s2[j]:
#                 lookup_table[i][j] = lookup_table[i - 1][j - 1] + 1
#             else:
#                 lookup_table[i][j] = max(lookup_table[i - 1][j], lookup_table[i][j - 1])
#     print(lookup_table)
#     return None
