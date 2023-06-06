#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 15:01:07 2023

@author: johnmorgan
"""

def lemonade_change(bills):
    fives, tens, twenties = 0, 0, 0
    for bill in bills:
        if bill == 5:
            fives += 1
        if bill == 10:
            if fives == 0:
                return False
            else:
                fives -= 1
                tens += 1
        if bill == 20:
            if tens > 0 and fives > 0:
                fives -= 1
                tens -= 1
                twenties += 1
            elif fives >= 3:
                fives -= 3
                twenties += 1
            else:
                return False
    return True
