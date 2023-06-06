#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:10:51 2022

@author: johnmorgan
"""

def get_damages(H):
    D = [1 for _ in H]
    H2 = [(H[i], i) for i in range(len(H))]
    def merge_sort(A, a = 0, b = None):
        if b is None: b = len(A)
        if 1 < b - a:
            c = (a + b + 1) // 2
            merge_sort(A, a, c)
            merge_sort(A, c, b)
            i, j, L, R = 0, 0, A[a:c], A[c:b]
            while a < b:
                if (j >= len(R)) or (i < len(L) and L[i][0] <= R[j][0]):
                    D[L[i][1]] += j
                    A[a] = L[i]
                    i += 1
                else:
                    A[a] = R[j]
                    j += 1
                a += 1
    merge_sort(H2)
    return D

print(get_damages([5, 2, 3, 4, 8, 1]))