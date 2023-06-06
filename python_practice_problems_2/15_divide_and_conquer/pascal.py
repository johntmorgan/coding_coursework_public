#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:48:16 2023

@author: johnmorgan
"""

# Time complexity O(line_number)

def pascal_triangle_recursive(line_number, space):
    current_line_size = line_number
    previous_line_size = current_line_size - 1
    if line_number == 1:
        current_line = [0] * current_line_size # Creating a list of size = current_line_size
        current_line[0] = 1
        return current_line
    else:
        current_line = [0] * current_line_size
        previous_line = pascal_triangle_recursive(line_number - 1, space + 1)
        for numIndex in range(current_line_size):
            if (numIndex - 1) >= 0:
                left_coefficient = previous_line[numIndex - 1]
            else:
                left_coefficient = 0
            if numIndex < previous_line_size:
                right_coefficient = previous_line[numIndex]
            else:
                right_coefficient = 0
            current_line[numIndex] = left_coefficient + right_coefficient
  
    for i in range(space):
        print(" ", end = " ")
    print (previous_line)
  
    return current_line

pascal_triangle_recursive(51, 1)