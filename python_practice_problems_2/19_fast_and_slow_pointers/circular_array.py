#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 14:29:32 2023

@author: johnmorgan
"""

# Naive: traverse array and look for cycle at every element
# O(n^2) time complexity, O(n) space complexity to track visited

# Fast/slow: O(n^2) time, O(1) space

def advance_pointer(arr, pointer):
    start = arr[pointer]
    pointer = (pointer + arr[pointer]) % len(arr)
    if arr[pointer] > 0 and start < 0 or arr[pointer] < 0 and start > 0:
        return pointer, False
    else:
        return pointer, True
    
def circular_array_loop(arr):  
    for index in range(len(arr)):
        no_reverse, fail = True, False
        fast, slow = index, index
        slow, no_reverse = advance_pointer(arr, slow)
        if not no_reverse:
            fail = True
        fast, no_reverse = advance_pointer(arr, fast)
        if not no_reverse:
            fail = True
        fast, no_reverse = advance_pointer(arr, fast)
        if not no_reverse:
            fail = True
        while fast != slow and not fail:
            slow, no_reverse = advance_pointer(arr, slow)
            if not no_reverse:
                fail = True
            fast, no_reverse = advance_pointer(arr, fast)
            if not no_reverse:
                fail = True
            fast, no_reverse = advance_pointer(arr, fast)
            if not no_reverse:
                fail = True
        if fast == slow:
            return True
    return False


arr = [1,3,-2,-4,1]
print(circular_array_loop(arr))

arr = [2,1,-1,-2]
print(circular_array_loop(arr))

arr = [3, 3, 1, -1, 2]
print(circular_array_loop(arr))