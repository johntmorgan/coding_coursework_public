#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:08:11 2023

@author: johnmorgan
"""

def climb_stairs(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 2
    ways = [0] * num
    ways[0] = 1
    ways[1] = 2
    for i in range(2, num):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[num - 1]


print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))