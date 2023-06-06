#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 17:24:38 2023

@author: johnmorgan
"""

from heapq import *
from collections import defaultdict

# O(n) - is O(nlog(c)) - c is chars in alphabet which is constant
# O(1) space - again from O(c)

def reorganize_string(input_string):
    freq = defaultdict(int)
    for char in input_string:
        freq[char] += 1
    heap = []
    for item in freq.items():
        heappush(heap, (-item[1], item[0]))
    output = ""
    while len(heap) > 0:
        curr = heappop(heap)
        if len(output) == 0 or output[-1] != curr[1]:
            output += curr[1]
            if -curr[0] > 1:
                heappush(heap, (curr[0] + 1, curr[1]))
        else:
            if len(heap) == 0:
                return ""
            else:
                curr2 = heappop(heap)
                output += curr2[1]
                output += curr[1]
                if -curr[0] > 1:
                    heappush(heap, (curr[0] + 1, curr[1]))
                if -curr2[0] > 1:
                    heappush(heap, (curr2[0] + 1, curr2[1]))
    return output

input_string = "abb"
print(reorganize_string(input_string))
input_string = "aaaaabbbbbb"
print(reorganize_string(input_string))
input_string = "aaaaabbbbbbb"
print(reorganize_string(input_string))
input_string = "abbb"
print(reorganize_string(input_string))
input_string = "jjjjj"
print(reorganize_string(input_string))
input_string = "hello"
print(reorganize_string(input_string))
input_string = "hellllo"
print(reorganize_string(input_string))