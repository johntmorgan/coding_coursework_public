#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:47:44 2023

@author: johnmorgan
"""

def unique_paths(m, n):
    paths = [[0] * n for _ in range(m)]
    paths[0][0] = 1
    for i in range(0, m):
        for j in range(0, n):
            if i > 0 and j > 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
            elif j > 0:
                paths[i][j] = paths[i][j - 1]
            elif i > 0:
                paths[i][j] = paths[i - 1][j]
    return paths[m - 1][n - 1]


print(unique_paths(2,3))
print(unique_paths(3,4))
print(unique_paths(3,7))