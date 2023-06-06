#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:19:40 2023

@author: johnmorgan
"""

def matchstick_to_square(matchsticks):
    if len(matchsticks) < 4:
        return False
    if sum(matchsticks) % 4 != 0:
        return False
    if sum(matchsticks) < 4:
        return False
    matchsticks.sort()
    matchsticks.reverse()
    pointer, end, sides, side_len = 0, len(matchsticks) - 1, 0, sum(matchsticks) // 4
    while pointer < end:
        if matchsticks[pointer] == side_len:
            pointer += 1
            sides += 1
        else:
            curr_sum = matchsticks[pointer]
            while curr_sum < side_len:
                curr_sum += matchsticks[end]
                end -= 1
                if end == pointer:
                    break
            if curr_sum > side_len or curr_sum < side_len:
                return False
            else:
                pointer += 1
                sides += 1
    return sides == 4


matchsticks = [1,1,1,1,2,2]
print(matchstick_to_square(matchsticks))