#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:01:25 2023

@author: johnmorgan
"""

# Stacks! Very quick review

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
                    
                
asteroids = [1,2,5,-4]
print(asteroid_collisions(asteroids))
asteroids = [3, -3]
print(asteroid_collisions(asteroids))
asteroids = [-1,2,2,-3]
print(asteroid_collisions(asteroids))
asteroids = [3,-9,1,3,2,5]
print(asteroid_collisions(asteroids))