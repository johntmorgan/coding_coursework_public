#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:54:51 2023

@author: johnmorgan
"""

# Lazy, just iterate over string

def convert_to_bin(n):
    n = int(n, 2)
    n = '{:032b}'.format(n)
    return n

def number_of_1_bits(n):
    n = convert_to_bin(n)
    count = 0
    for field in n:
        if field == "1":
            count += 1
    return count

num = "0b00000000000000000000000000001011"
print(number_of_1_bits(num))

def convert_to_bin(n):
    n = int(n, 2)
    n = '{:032b}'.format(n)
    return n

def number_of_1_bits(n):
    n = convert_to_bin(n)
    return n.count("1")

num = "0b00000000000000000000000000001011"
print(number_of_1_bits(num))


def count_set_bits(n):
    # base case
    if (n == 0) or len(n) == 0:
        return 0
    else:
        return (int(n[-1]) & 1) + count_set_bits(n[:-1])

def convert_to_bin(n):
    n = int(n, 2)
    n = '{:032b}'.format(n)
    return n

def number_of_1_bits(n):
    n = convert_to_bin(n)
    return count_set_bits(n)

num = "0b00000000000000000000000000001011"
print(number_of_1_bits(num))