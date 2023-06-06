#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:09:43 2023

@author: johnmorgan
"""

def asteroid_collisions(asteroids):
    pos_stack, neg_safe = [], []
    for val in asteroids:
        if val > 0:
            pos_stack.append(val)
        else:
            matched = False
            while pos_stack and not matched:
                curr = pos_stack[-1]
                if abs(curr) < abs(val):
                    pos_stack.pop()
                if abs(curr) == abs(val):
                    pos_stack.pop()
                    matched = True
                if abs(curr) > abs(val):
                    break
            if not pos_stack and not matched:
                neg_safe += [val]
    return neg_safe + pos_stack
    

asteroids = [3, 9, -6, -2, 1, 2]
print(asteroid_collisions(asteroids))

asteroids = [3, -9, 1, 3, 2, -5]
print(asteroid_collisions(asteroids))

def asteroid_collisions(asteroids):
    pos_stack, neg_safe = [], []
    for val in asteroids:
        if val > 0:
            pos_stack.append(val)
        else:
            matched, exploded = False, False
            while pos_stack and not matched and not exploded:
                if abs(val) > pos_stack[-1]:
                    pos_stack.pop()
                elif abs(val) == pos_stack[-1]:
                    pos_stack.pop()
                    matched = True
                else:
                    exploded = True
            if not matched and not exploded:
                neg_safe.append(val)
    return neg_safe + pos_stack