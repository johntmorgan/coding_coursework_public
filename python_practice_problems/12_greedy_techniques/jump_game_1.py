#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:01:39 2023

@author: johnmorgan
"""

# Review, easy but struggled a bit

def jump_game(nums):
    target = len(nums) - 1
    curr = len(nums) - 2
    while curr >= 0:
        if nums[curr] + curr >= target:
            target = curr
        curr -= 1
    if target == 0:
        return True
    return False

nums = [2,3,1,1,9]
print(jump_game(nums))