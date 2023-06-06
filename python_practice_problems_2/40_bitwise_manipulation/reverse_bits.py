#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:12:13 2023

@author: johnmorgan
"""

# Review

def reverse_bits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result
            
print(reverse_bits(5))