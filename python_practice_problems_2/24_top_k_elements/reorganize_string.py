#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:22:19 2023

@author: johnmorgan
"""

# importing libraries
from collections import Counter
from heapq import *

# O(nlog(c)) - c is number of chars in string
# C is upper bounded by number of letters in alphabet, so log(c) is a constant
# Time complexity O(n)
 
# O(c) extra space, but again -> O(1)

def reorganize_string(input_string):
    freq = {}
    for char in input_string:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1
    heap = []
    for key, value in freq.items():
        heappush(heap, [-value, key])
    output = ""
    while len(heap) > 0:
        if len(output) == 0 or heap[0][1] != output[-1]:
            new_char = heappop(heap)
        else:
            if heap[0][1] == output[-1] and len(heap) == 1:
                return ""
            else:
                repeat = heappop(heap)
                new_char = heappop(heap)
                heappush(heap, repeat)
        output += new_char[1]
        if new_char[0] < -1:
            heappush(heap, [(new_char[0] + 1), new_char[1]])
    return output
        

input_string = "aba"
print(reorganize_string(input_string))

input_string = "aaabc"
print(reorganize_string(input_string))

input_string = "aaaaabbbbbbb"
print(reorganize_string(input_string))