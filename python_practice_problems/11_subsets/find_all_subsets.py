#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:25:08 2023

@author: johnmorgan
"""

def find_all_subsets(v):
    result = [[]]
    for elem in v:
        for _ in range(len(result)):
            existing = result.pop(0)
            result.append(existing)
            result.append(existing + [elem])
    return result
    
    
v = [1]
print(find_all_subsets(v))

v = [1,2]
print(find_all_subsets(v))