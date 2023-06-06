#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:53:34 2023

@author: johnmorgan
"""

# Review
# Time O(n)
# Space O(1)

def two_single_numbers(arr):
    bitwise_sum = 0
    for i in arr:
        bitwise_sum ^= i

    # the least significant bit can be found with number ^ (-number)
    bitwise_mask = bitwise_sum & (-bitwise_sum)

    # divide into two groups of numbers, here we want the group with bit set
    # which results in one of the numbers we want due to the property X ^ X = 0
    results = 0
    for i in arr:
        if bitwise_mask & i:
            results = results ^ i

    return [results, bitwise_sum ^ results]
