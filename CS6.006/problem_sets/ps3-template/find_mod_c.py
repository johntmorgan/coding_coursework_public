#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:44:35 2022

@author: johnmorgan
"""

def find_mod_c(A):
    mod_c = 1
    while True:
        match = True
        vals = []
        for elem in A:
            val = ((10 * elem + 4) % mod_c) % 7
            if val in vals:
                match = False
            else:
                vals += [val]
        if match == True:
            return mod_c
        else:
            print(mod_c)
            mod_c += 1

def test_mod_c(A, mod_c):
    for elem in A:
        print(((10 * elem + 4) % mod_c) % 7)

A = [47, 61, 36, 52, 56, 33, 92]
# print(find_mod_c(A))
test_mod_c(A, 13)