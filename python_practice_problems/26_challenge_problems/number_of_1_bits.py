#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:00:54 2023

@author: johnmorgan
"""

def number_of_1_bits(n):
    bits = 0
    n = int(n, 2)
    while n:
        if n & 1:
            bits += 1
        n >>= 1
    return bits

    
print(number_of_1_bits(5))