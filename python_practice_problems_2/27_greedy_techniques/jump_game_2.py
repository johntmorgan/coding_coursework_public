#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:44:54 2023

@author: johnmorgan
"""

def jump_game_two(nums):
    if len(nums) == 1:
        return 0
    farthest = 0
    current = 0
    jumps = 0
    for i in range(len(nums)):
        farthest = max(farthest, i + nums[i])
        if i == current:
            jumps += 1
            current = farthest
        if current == len(nums) - 1:
            return jumps
    return jumps

nums = [2,3,1,1,9]
print(jump_game_two(nums))