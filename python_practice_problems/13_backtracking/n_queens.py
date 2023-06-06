#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:00:33 2023

@author: johnmorgan
"""

# O(n^n) time
# O(n) space

def valid_placement(curr, col):
    if col in curr:
        return False
    row = len(curr) + 1
    for i in range(len(curr)):
        placed_col = curr[i]
        placed_row = i + 1
        if placed_col + (row - placed_row) == col:
            return False
        if placed_col - (row - placed_row) == col:
            return False
    return True

def recurse_placement(valid, curr, n):
    if len(curr) == n:
        valid.append(curr)
    else:
        for col in range(n):
            if valid_placement(curr, col):
                curr.append(col)
                recurse_placement(valid, curr, n)
                curr.pop()
            
def solve_n_queens(n):
    valid = []
    recurse_placement(valid, [], n)
    return len(valid)
    
print(solve_n_queens(1))
print(solve_n_queens(2))
print(solve_n_queens(3))
print(solve_n_queens(4))
print(solve_n_queens(5))
print(solve_n_queens(6))