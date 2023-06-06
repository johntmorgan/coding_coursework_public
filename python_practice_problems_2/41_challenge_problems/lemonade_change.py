#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:36:17 2023

@author: johnmorgan
"""

def lemonade_change(bills):
    fives, tens, twenties = 0, 0, 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives >= 1:
                tens += 1
                fives -= 1
            else:
                return False
        elif bill == 20:
            if tens >= 1 and fives >= 1:
                tens -= 1
                fives -= 1
                twenties += 1
            elif fives >= 3:
                fives -= 3
                twenties += 1
            else:
                return False
    return True

bills = [5,10,5,5,10,20]
print(lemonade_change(bills))
bills = [5,5,5,5,20,10,10]
print(lemonade_change(bills))