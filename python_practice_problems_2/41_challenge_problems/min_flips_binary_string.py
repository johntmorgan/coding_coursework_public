#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:57:56 2023

@author: johnmorgan
"""

# Brute force O(n^2)

def min_flips(s):
    n = len(s)
    min_flips = float('inf')
    rotations = 0
    while rotations < n:
        flips = 0
        for index, digit in enumerate(s):
            if index % 2 == 0 and digit == "1":
                flips += 1
            if index %2 != 0 and digit == "0":
                flips += 1
        if flips < min_flips:
            min_flips = flips
        if n - flips < min_flips:
            min_flips = n - flips
        s = s[1:] + s[0]
        rotations += 1
    return min_flips

# Review O(n) solution
# Go through and count number of flips
# If str length is even you are done - moving a bit does nothing
# Take min of starting with 0 (flips counted) and starting from 1 (n - flips_counted)
# If str length is odd, moving may do something
# Curr_bit is back to 0, flipped an odd number of times, opposite last compare
# So now go through again, if you match curr_bit, you're saving on a flip
# If you don't match curr_bit, you're losing a flip
# Each time take min of current min_diff, improved flip_count, and n - flip_count

# def min_flips(s):
#     n = len(s)
#     flip_count = 0
#     curr_bit = 0
#     for c in s:
#         if int(c) != curr_bit:
#             flip_count += 1
#         curr_bit = not curr_bit
#     min_diff = min(flip_count, n - flip_count)
#     if n % 2 != 0:
#         for c in s:
#             if int(c) == curr_bit:
#                 flip_count -= 1
#             else:
#                 flip_count += 1
#             min_diff = min(min_diff, flip_count, n - flip_count)
#             curr_bit = not curr_bit
#     return min_diff    


s = "010" #0
print(min_flips(s))

s = "1110" #1
print(min_flips(s))

s = "0010101" #0
print(min_flips(s))

s = "110011011" #3
print(min_flips(s))