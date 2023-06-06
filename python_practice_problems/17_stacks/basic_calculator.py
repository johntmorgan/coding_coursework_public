#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:45:26 2023

@author: johnmorgan
"""

def calculator(expression):
    stack = []
    result, sign, number = 0, 1, 0
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    exp = ["+", "-"]
    for char in expression:
        if char in digits:
            number = 10 * number + int(char)
        elif char in exp:
            result += number * sign
            if char == "-":
                sign = -1 
            else:
                sign = 1
            number = 0
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result, sign, number = 0, 1, 0
        elif char == ")":
            result += sign * number
            sign_pop = stack.pop()
            result_pop = stack.pop()
            result = result_pop + sign_pop * result
            number = 0
    return result + number * sign
    
    
expression = "12 - (6 + 2) + 5"
print(calculator(expression))