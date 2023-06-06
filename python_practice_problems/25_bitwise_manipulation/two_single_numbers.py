#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:44:17 2023

@author: johnmorgan
"""

def two_single_numbers(arr):
    bitwise_sum = 0
    # Bitwise sum is xor of two numbers
    for num in arr:
        bitwise_sum = bitwise_sum ^ num
    # Find first bit set to one, by taking & of 2's complement
    bitwise_mask = bitwise_sum & (-bitwise_sum)
    results = 0
    for num in arr:
        # If the bitwise mask intersects with number, include
        # Doubled nums cancel out
        # So you're left with one number
        if bitwise_mask & num:
            results = results ^ num
    # Return number and xor other number from bitwise sum
    return [results, bitwise_sum ^ results]