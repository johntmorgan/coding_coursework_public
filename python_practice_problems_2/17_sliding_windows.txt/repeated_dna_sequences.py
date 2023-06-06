#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:41:17 2023

@author: johnmorgan
"""

# Naive:
# Find first seq of required length
# Scan remaining string for any repetitions
# O(n^2 * k)

# Good: use dict
# Should be O(n)

def find_repeated_sequences(s, k):
    d = dict()
    for index in range(len(s)):
        if index + k < len(s) + 1:
            seq = s[index:index + k]
            if seq in d:
                d[seq] = d[seq] + 1
            else:
                d[seq] = 1
    result = set()
    for key in d.keys():
        if d[key] > 1:
            result.add(key)
    return result

# Better: use rolling hash to calculate
# AGCT = 1234
# In a 3-nucleotide window
# Multiply first position by 4^2, then 4^1, then 4^0
# Add value to set
# Add and subtract depending on nucleotide addition and removal
# O(n)
# O(n - k) space complexity

def find_repeated_sequences(s, k):
    window_size = k
    if len(s) <= window_size:
        return set()
    base = 4
    hi_place_value = pow(base, window_size)
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = hashing * base - \
                numbers[start - 1] * hi_place_value +\
                numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start: start + window_size])
        substring_hashes.add(hashing)
    return output

s, k = "AAAAACCCCCAAAAACCCCCC" , 8
print(find_repeated_sequences(s, k))
# s, k = "GGGGGGGGGGGGGGGGGGGGGGGGG" , 12
# print(find_repeated_sequences(s, k))
# s, k = "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT" , 10
# print(find_repeated_sequences(s, k))
# s, k = "AAAAAACCCCCCCAAAAAAAACCCCCCCTG" , 10
# print(find_repeated_sequences(s, k))
# s, k = "ATATATATATATATAT" , 6
# print(find_repeated_sequences(s, k))