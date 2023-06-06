#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:38:04 2023

@author: johnmorgan
"""

def sum_of_digits(num):
    num_str = str(num)
    num_sum = 0
    for str_digit in num_str:
        num_sum += int(str_digit) ** 2
    return num_sum

def is_happy_number(num):
    fast, slow = num, num
    while fast != 1:
        fast = sum_of_digits(sum_of_digits(fast))
        slow = sum_of_digits(slow)
        if fast == slow and fast != 1:
            return False
    return True


num = 2147483646
print(is_happy_number(num))

num = 1
print(is_happy_number(num))

num = 28
print(is_happy_number(num))

num = 4
print(is_happy_number(num))