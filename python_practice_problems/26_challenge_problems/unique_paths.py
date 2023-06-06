#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:52:58 2023

@author: johnmorgan
"""

def unique_paths(m, n):
    paths = [[0] * n] * m
    for i in range(n):
        paths[0][i] = 1
    for j in range(m):
        paths[j][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
    return paths[m - 1][n - 1]
    

print(unique_paths(2, 3))

print(unique_paths(3, 4))