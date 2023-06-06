#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:37:22 2023

@author: johnmorgan
"""

def climb_stairs(num):
    if num == 0 or num == 1:
        return 1
    if num == 2:
        return 2
    two_prior = 1
    one_prior = 2
    for _ in range(2, num):
        curr = two_prior + one_prior
        one_prior, two_prior = curr, one_prior
    return curr
    
print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(6))
print(climb_stairs(7))