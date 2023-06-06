#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:45:59 2023

@author: johnmorgan
"""

# O(n)
# O(1) space

def jump_game(nums):
    target = len(nums) - 1
    index = len(nums) - 1
    while index >= 0:
        if index + nums[index] >= target:
            target = index
        index -= 1
    if target == 0:
        return True
    return False

nums = [2,3,1,1,9]
print(jump_game(nums))
nums = [2,3,1,0,9]
print(jump_game(nums))
nums = [2,0,1,0,9]
print(jump_game(nums))