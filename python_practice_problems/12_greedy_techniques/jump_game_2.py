#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:09:26 2023

@author: johnmorgan
"""

# Review
# Got tangled due to dizziness, had to look at hint

def jump_game_two(nums):
    if len(nums) == 1:
        return 0
    jumps, curr, best = 0, 0, 0
    for i in range(len(nums)):
        best = max(best, i + nums[i])
        if i == curr:
            jumps += 1
            curr = best
            if curr >= len(nums) - 1:
                break
    return jumps
            

nums = [2,3,1,1,9]
print(jump_game_two(nums))

nums = [3,2,1,1,4]
print(jump_game_two(nums))

nums = [1,2,2,0,4]
print(jump_game_two(nums))