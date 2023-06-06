#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:18:24 2022

@author: johnmorgan
"""

def count_paths(F):
    n = len(F)
    K = [[-float('inf')] * (n + 1) for _ in range(n + 1)]
    X = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range (1, n + 1):
        for j in range(1, n + 1):
            if F[i - 1][j - 1] == 't':
                continue
            if i == 1 and j == 1:
                K[1][1], X[1][1] = 0, 1
                continue
            if F[i - 1][j - 1] == 'm':
                m = 1
            else:
                m = 0
            K[i][j] = m + max(K[i - 1][j], K[i][j - 1])
            if K[i - 1][j] + m == K[i][j]: X[i][j] += X[i - 1][j]
            if K[i][j - 1] + m == K[i][j]: X[i][j] += X[i][j - 1]
    return X[n][n]
            