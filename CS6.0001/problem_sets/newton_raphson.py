#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:25:08 2022

@author: johnmorgan
"""

epsilon = 0.01
k = float(input("Enter number to find root of: "))
guess = k / 2.0
steps = 0

while abs(guess*guess - k) > epsilon:
    guess = guess - ((guess**2 - k) / (2 * guess))
    steps += 1
    
print ("Square root of", k, "is about", guess)
print ("Number of steps:", steps)