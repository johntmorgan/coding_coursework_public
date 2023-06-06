#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:30:33 2022

@author: johnmorgan
"""

epsilon = 0.01
k = float(input("Enter number to find root of: "))
guess = k / 2.0
low = 0
high = k
steps = 0

while abs(guess*guess - k) > epsilon:
    if (guess * guess) > k:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
    steps += 1
    
print ("Square root of", k, "is about", guess)
print ("Number of steps:", steps)