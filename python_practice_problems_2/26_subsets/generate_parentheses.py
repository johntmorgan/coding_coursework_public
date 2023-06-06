#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:39:34 2023

@author: johnmorgan
"""

# Time analysis
# Think of it like a branching tree, branching b depth m
# 1 + b + b^2 + b^(m - 1)
# Geometric sequence
# Evaluates to O(b^m)
# Here branching is 2, max depth is 2n
# O(2^2n) # Review
# O(n) space complexity, max stack size 2n


def recurse_combo(n, cstr, op, cl, result):
    if op == n and cl == n:
        result.append(cstr)
        return
    else:
        if op == cl:
            recurse_combo(n, cstr + "(", op + 1, cl, result)
        else:
            if op < n:
                recurse_combo(n, cstr + "(", op + 1, cl, result)
            recurse_combo(n, cstr + ")", op, cl + 1, result)
        
def generate_combinations(n):
    result = []
    recurse_combo(n, "", 0, 0, result)
    return result

print(generate_combinations(2))
