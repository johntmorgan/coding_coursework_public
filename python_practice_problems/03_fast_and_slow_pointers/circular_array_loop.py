#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:07:59 2023

@author: johnmorgan
"""

def advance_pointer(pointer, arr, n):
    loc = pointer
    curr = arr[pointer]
    pointer = (pointer + arr[pointer]) % n
    if curr * arr[pointer] < 0 or loc == pointer:
        return pointer, False
    return pointer, True

def advance_fast_slow(fast, slow, arr, n):
    valid = True
    fast, valid = advance_pointer(fast, arr, n)
    if valid:
        fast, valid = advance_pointer(fast, arr, n)
    if valid:
        slow, valid = advance_pointer(slow, arr, n)
    return fast, slow, valid

def circular_array_loop(arr):
    n = len(arr)
    for index in range(n):
        fast, slow = index, index
        fast, slow, valid = advance_fast_slow(fast, slow, arr, n)
        while fast != slow and valid:
            fast, slow, valid = advance_fast_slow(fast, slow, arr, n)
        if valid:
            return True
    return False


arr = [1,3,-2,-4,1]
print(circular_array_loop(arr))

arr = [1,3,-2,-4,-1]
print(circular_array_loop(arr))

arr = [1, 4, 2, 3, 1]
print(circular_array_loop(arr))

arr = [3, 3, 1, -1, 2]
print(circular_array_loop(arr))