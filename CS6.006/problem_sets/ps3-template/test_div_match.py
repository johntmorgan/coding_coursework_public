#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:11:48 2022

@author: johnmorgan
"""

def test_div_match_basic_mod(k):
    a = 1
    while a <= 100:
        print(((10 * (k * a) + 4)) % k)
        a += 1

# test_div_match_basic_mod(8)
            
def test_div_match_mod():
    a = 7
    n = 100
    u = 4000
    k = 500
    while k <= u:
        print((((k * n) // u) + a) % n)
        k += 1

# test_div_match_mod()

def test_div_match_mod_raw():
    a = 7
    n = 100
    u = 4000
    k = 519
    # print(k * n // u)
    # print((k * n // u) % n)
    print((((k * n) // u) + a) % n)
        
test_div_match_mod_raw()