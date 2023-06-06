#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 15:55:24 2023

@author: johnmorgan
"""

from math import log2, floor

# Review
# O(1) time and space

def find_bitwise_complement(num):
    if num == 0:
        return 1
    bit_count = floor(log2(num)) + 1
    all_bits_set = pow(2, bit_count) - 1
    return num ^ all_bits_set


print(find_bitwise_complement(42))