#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:48:36 2023

@author: johnmorgan
"""

# If m > n, then GCD(m, n) == GCD(m - n, n)
# If m/d and n/d leave no remainder, then (m - n) / d has no remainder

def gcd(var1, var2):
    if var1 == 0:
        return var2
    return gcd(var2 % var1, var1)


var1, var2 = 6, 9
print(gcd(var1, var2))