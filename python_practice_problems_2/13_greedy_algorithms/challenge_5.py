#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:08:49 2023

@author: johnmorgan
"""

def find_largest_number(number_of_digits, sum_of_digits):
    result = []
    num = number_of_digits
    left = sum_of_digits
    while left > 0:
        for i in range(9, -1, -1):
            while left >= i and num > 0:
                result += [i]
                left -= i
                num = num - 1
            if num < 0:
                print("Number:",num)
                return [-1]
        if left > 0:
            print("Left:", left)
            return [-1]
    return result
    
# Course solution, more terse, less iteration
# Review
# O(n), find in one iteration

def find_largest_number(number_of_digits, sum_of_digits):
    if sum_of_digits == 0:
        if number_of_digits == 1:
            return [0]
        else:
            return [-1]
    if sum_of_digits > 9 * number_of_digits:
        return [-1]
    result = [0] * number_of_digits
    for i in range(number_of_digits):
        if sum_of_digits >= 9:
            result[i] = 9
            sum_of_digits -= 9
        else:
            result[i] = sum_of_digits
            sum_of_digits = 0
    return result

sum_of_digits = 20
number_of_digits = 3
print(find_largest_number(number_of_digits, sum_of_digits))
