#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:36:34 2023

@author: johnmorgan
"""

# Review

def integer_addition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a