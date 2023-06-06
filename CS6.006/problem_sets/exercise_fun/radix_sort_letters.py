#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:59:09 2022

@author: johnmorgan
"""

def counting_sort(A):
    "Sort A assuming items have non-negative keys"
    u = 1 + max([x.key for x in A])
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chain in D:
        for x in chain:
            A[i] = x
            i += 1

# really just tuple sort now
def tuple_sort_strings(A):
    "Sort A assuming items have non-negative keys"
    n = len(A)
    c = len(A[0])
    class Obj: pass
    D = [Obj() for a in A]
    # Make reversed letter tuples
    for i in range(n):
        D[i].digits = []
        D[i].item = A[i]
        for j in range(c): 
            D[i].digits.append(A[i][len(A[i]) - j - 1])
    for i in range(c): 
        for j in range(n):
            D[j].key = ord(D[j].digits[i])
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item
        
strings = ["aeiou", "uoiea", "eaiou", "euioa", "iouae", "ouaei"]
tuple_sort_strings(strings)
print(strings)