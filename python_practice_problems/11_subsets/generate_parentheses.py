#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:11:31 2023

@author: johnmorgan
"""

# O(4^n) time - branching 2 at each step, depth of 2n - both opening and closing
# O(n) space complexity

def recurse_combo(result, target, curr, open_num, close_num):
    if open_num == target and close_num == target:
        result.append(curr)
    else:
        if open_num <= close_num:
            recurse_combo(result, target, curr + "(", open_num + 1, close_num)
        else:
            recurse_combo(result, target, curr + ")", open_num, close_num + 1)
            if open_num < target:
                recurse_combo(result, target, curr + "(", open_num + 1, close_num)

def generate_combinations(n):
    result = []
    recurse_combo(result, n, "", 0, 0)
    return result


n = 3
print(generate_combinations(n))