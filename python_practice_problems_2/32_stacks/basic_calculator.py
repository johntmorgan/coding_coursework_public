#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:48:55 2023

@author: johnmorgan
"""

# Review
# Track current number with curr
# If you hit a sign, evaluate curr according to prior sign, then update
# If you hit an open paren, push result and sign onto stack
# If you hit a close parent, eval result from inside paren * stack sign + stack result
# Time O(n)
# Space(O(n))

def calculator(expression):
    stack = []
    curr = 0
    sign = 1
    result = 0
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    exp = ["+", "-"]
    for index in range(len(expression)):
        char = expression[index]
        if char in nums:
            curr = curr * 10 + int(char)
        elif char in exp:
            result += curr * sign
            sign = -1 if char == "-" else 1
            curr = 0
        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result, sign = 0, 1
        elif char == ")":
            result += sign * curr
            pop_sign = stack.pop()
            stored = stack.pop()
            result = result * pop_sign + stored
            curr = 0
        else:
            pass
    return result + curr * sign



expression = "12 - (6 + 2) + 5"
print(calculator(expression))

expression = "(8 + 100) + (13 - 8 - (2 + 1))"
print(calculator(expression))