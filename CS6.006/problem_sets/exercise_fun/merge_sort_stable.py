#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:24:04 2022

@author: johnmorgan
"""

def merge_sort(A, a = 0, b = None): # Sort sub-array A[a:b]
    if b is None:
        b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)
        L, R = A[a:c], A[c:b]
        i, j = 0, 0
        while a < b:
            if (j >= len(R)) or (i < len(L) and L[i] <= R[j]):
                A[a] = L[i]
                i = i + 1
            else:
                A[a] = R[j]
                j = j + 1
            a = a + 1
    
A = [8, 3, 7, 1, 1, 2, 9, 4]
merge_sort(A)
print(A)