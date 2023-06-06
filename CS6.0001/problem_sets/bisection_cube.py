#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:05:40 2022

@author: johnmorgan
"""

cube = float(input("Enter number to find root of: "))

epsilon = .01
guess = 0.0
low = 0.0
high = cube
num_guesses = 0

# Make code work for fractions and negative numbers
if cube < 1.0 and cube > 0.0:
    high = 1.0
elif cube < 0.0 and cube > -1.0:
    high = 0.0
    low = -1.0
elif cube < 0.0:
    high = 0.0
    low = cube

while abs(guess**3 - cube) > epsilon:
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (low + high) / 2.0
    num_guesses += 1
if abs(guess**3 - cube) < epsilon:    
    print("The approximate cube root of", cube, "is", guess)
else:
    print ("Failed to find cube root of", cube)
print("The number of guesses was", num_guesses)