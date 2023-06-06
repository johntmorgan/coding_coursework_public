#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:32:30 2022

@author: johnmorgan
"""

cube = float(input("Enter number to find root of: "))

# for guess in range(cube + 1):
#     if guess**3 == cube:
#         print("The cube root of", cube, "is", guess)

# Cover negative cubes
# Tell user if no perfect cube
# for guess in range(abs(cube) + 1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 == abs(cube):
#     if cube < 0:
#         guess = -guess
#     print("The cube root of", cube, "is", guess)
# else:
#     print(cube, "is not a perfect cube")

# Approximate solution

# epsilon = .1
# increment = .01
# guess = 0.0
# num_guesses = 0

# while abs(guess**3 - cube) > epsilon and guess < cube:
#     guess += increment
#     num_guesses += 1
# if abs(guess**3 - cube) < epsilon:    
#     print("The approximate cube root of", cube, "is", guess)
# else:
#     print ("Failed to find cube root of", cube)
# print("The number of guesses was", num_guesses)

