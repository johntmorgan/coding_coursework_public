#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:25:27 2023

@author: johnmorgan
"""

def recurse_match(matchsticks, side_len, sides, solved):
    if matchsticks == [] and sides == 4:
        solved += [1]
    else:
        if matchsticks[0] == side_len:
            matchsticks.pop()
            recurse_match(matchsticks, side_len, sides + 1, solved)
        elif matchsticks[0] < side_len:
            if side_len - matchsticks[0] in matchsticks:
                matchsticks.pop(matchsticks.index(side_len - matchsticks[0]))
                matchsticks.pop(0)
                recurse_match(matchsticks, side_len, sides + 1, solved)
            else:
                return False
        else:
            return False
        
def matchstick_to_square(matchsticks):
    if len(matchsticks) < 4:
        return False
    match_sum = sum(matchsticks)
    if match_sum < 4:
        return False
    if match_sum % 4 != 0:
        return False
    matchsticks.sort()
    side_len = match_sum / 4
    solved = []
    recurse_match(matchsticks, side_len, 0, solved)
    if len(solved) > 0:
        return True
    return False

matchsticks = [1,1,2,2,2]
print(matchstick_to_square(matchsticks))

matchsticks = [3,3,3,3,4]
print(matchstick_to_square(matchsticks))