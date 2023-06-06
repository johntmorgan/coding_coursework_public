#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:05:38 2023

@author: johnmorgan
"""

# Ok, but uses array
# O(n) time complexity
# O(n) space

def find_tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    trib_array = [-1] * (n + 1)
    trib_array[0] = 0
    trib_array[1] = 1
    trib_array[2] = 1
    index = 3
    while trib_array[n] < 0:
        trib_array[index] = trib_array[index - 3] + trib_array[index - 2] + \
            trib_array[index - 1]
        index += 1
    return trib_array[n]

# Better
# O(n) time
# O(1) space
# Review

def find_tribonacci(n):
    if n < 3:
        return 1 if n else 0
    first_num, second_num, third_num = 0, 1, 1
    for _ in range(n - 2):
        first_num, second_num, third_num = second_num, third_num, \
          first_num + second_num + third_num
    return third_num

print(find_tribonacci(10))