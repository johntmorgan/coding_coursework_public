#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:42:54 2023

@author: johnmorgan
"""

# Naive approach
# Repeatedly calculate squared sum, store in hash set
# If already in set, have detected cycle, return False
# Good for small numbers
# May get infeasible for large ones
# Time complexity O(logn), space complexity O(n)

# Good approach
# O(logn) again
# Space complexity O(1) - don't need any extra

def sum_of_digits(n):
    strn = list(str(n))
    strsum = 0
    for elem in strn:
        strsum += pow(int(elem), 2)
    return strsum

def is_happy_number(n):
    slow = n
    fast = sum_of_digits(n)
    while fast != 1:
        slow = sum_of_digits(slow)
        fast = sum_of_digits(sum_of_digits(fast))
        if slow == fast:
            return False
    return True

n= 28
print(is_happy_number(n))
n = 4
print(is_happy_number(n))
n = 2147483646
print(is_happy_number(n))
n = 1
print(is_happy_number(n))
n = 19
print(is_happy_number(n))
n = 8
print(is_happy_number(n))
n = 7
print(is_happy_number(n))