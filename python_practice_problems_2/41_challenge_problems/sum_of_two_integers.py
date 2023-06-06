#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:25:23 2023

@author: johnmorgan
"""

# Review
# Set carry column
# Set a = non carried

def integer_addition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
    
a = 1
b = 2
print(integer_addition(a, b))

a = 1
b = 5
print(integer_addition(a, b))