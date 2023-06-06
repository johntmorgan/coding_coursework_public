#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:30:18 2023

@author: johnmorgan
"""

# Naive
# O(n * 2^n)

def find_all_subsets(v):
    result = [[]]
    for elem in v:
        for index in range(len(result)):
            result.append(result[index] + [elem])
    return result

# Optimized binary number approach method
# Still O(2^n * n) though... exactly what does this save?
# Space O(n)... my solution is the same
# Hmm.

def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
        return 0
    return 1

def find_all_subsets(v):
    sets = []
    if not v:
        return [[]]
    else:
        subsets_count = 2 ** len(v)
        for i in range(0, subsets_count):
            st = set()
            for j in range(0, len(v)):
                if get_bit(i, j) == 1 and v[j] not in st:
                    st.add(v[j])
            if i == 0:
                sets.append([])
            else:
                sets.append(list(st))
    return sets

v = [1, 2]
print(find_all_subsets(v))

v = [2,5,7]
print(find_all_subsets(v))