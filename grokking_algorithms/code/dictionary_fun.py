#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:53:42 2022

@author: johnmorgan
"""

book = dict()
book["apple"] = 0.67
book["milk"]= 1.65

print(book["apple"])
print(book["milk"])

# book = {}


voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out")
    else:
        voted[name] = True
        print("Let them vote")
        
check_voter("Tom")
check_voter("John")
check_voter("Tom")