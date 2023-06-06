#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:57:44 2023

@author: johnmorgan
"""

# Review - remember to use set
# O(n - k + 1) time and space

def find_repeated_sequences(s, k):
    seqs = set()
    output = []
    for start in range(0, len(s) - k + 1):
        seq = s[start:start + k]
        if seq in seqs and seq not in output:
            output.append(seq)
        elif seq not in seqs:
            seqs.add(seq)
    return output


s = "AAAAACCCCCAAAAACCCCCC"
k = 8
print(find_repeated_sequences(s, k))

